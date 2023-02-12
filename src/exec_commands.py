
def get_commands(filepath):
    with open(filepath) as file:
        commands = [line for line in file.read().split(';')][:-1]
    return commands


def exec_commands(commands, conn, is_dql):
    curs = conn.cursor()
    for i, command in enumerate(commands):
        try:
            curs.execute(command)
        except Exception as msg:
            print(f'error with command no {i}: {msg}')
    if not is_dql:
        conn.commit()
    if conn is not None:
        conn.close()
