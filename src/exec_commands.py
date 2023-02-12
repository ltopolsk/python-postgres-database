from psycopg2 import OperationalError
import psycopg2.errors


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
            print(f'command no {i} skipped due to operational error: {msg}')
        except psycopg2.errors.DuplicateTable as msg:
            print(f"error: {str(msg).rstrip()}, skipping command no {i}") 
    if not is_dql:
        conn.commit()
    if conn is not None:
        conn.close()
