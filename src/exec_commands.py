
from psycopg2 import OperationalError


def get_commands(filepath):
    with open(filepath) as file:
        commands = [line for line in file.read().split(';')][:-1]
    return commands


def exec_commands(commands, conn, is_dql):
    curs = conn.cursor()
    for i, command in enumerate(commands):
        try:
            curs.execute(command)
        except OperationalError as msg:
            print(f'OperationalError with command no {i}: {msg}')
        except Exception as e:
            raise e
        # finally:
    if not is_dql:
        conn.commit()
    if curs is not None:
        curs.close()
