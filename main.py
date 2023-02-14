from src.config import config
from src.exec_commands import get_commands, exec_commands
from src.connect import get_connection
from src.parse_data import read_csv, insert_podroze
import os


if __name__ == "__main__":

    lines = read_csv(os.path.join('data', 'Podroze.csv'))
    # print(list(next(lines).keys())[0])
    conn = get_connection(config())
    insert_podroze(lines, conn)
    if conn is not None:
        conn.close()

    # for file in ('insert_data.sql',):
    #     conn = get_connection(config())
    #     commands = get_commands(os.path.join('./sql_scripts', file))
    #     exec_commands(commands, conn, False)
    # # conn.close()
