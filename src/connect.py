import psycopg2
from src.config import config
from src.exec_commands import get_commands, exec_commands


def get_connection(params):
    return psycopg2.connect(**params)


if __name__ == "__main__":
    conn = get_connection(config())
    commands = get_commands('create_table.ddl')
    exec_commands(commands, conn, False)
    conn.close()