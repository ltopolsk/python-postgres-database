from src.config import config
from src.exec_commands import get_commands, exec_commands
from src.connect import get_connection
import os

if __name__ == "__main__":

    for file in ('remove_tables.sql', 'create_tables.sql', 'data.sql'):
        conn = get_connection(config())
        commands = get_commands(os.path.join('./sql_scripts', file))
        exec_commands(commands, conn, False)
    # conn.close()
