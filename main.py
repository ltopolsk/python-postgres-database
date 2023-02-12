from src.config import config
from src.exec_commands import get_commands, exec_commands
from src.connect import get_connection

if __name__ == "__main__":
    conn = get_connection(config())
    commands = get_commands('.\sql_scripts\create_tables.ddl')
    exec_commands(commands, conn, False)
    conn.close()