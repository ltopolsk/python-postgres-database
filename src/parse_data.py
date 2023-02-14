import datetime
# from psycopg2 import sql
from psycopg2.extensions import AsIs
from src.row import PodrozeRow


def read_csv(filepath):
    lines = (line for line in open(filepath))
    list_line = (s.rstrip().split(',') for s in lines)
    col_names = next(list_line)
    return (dict(zip(col_names, data)) for data in list_line)


def get_date(formated_date, split_char="/"):
    vals = formated_date.split(split_char)
    return datetime.date(int(vals[2]), int(vals[0]), int(vals[1]))


def insert_podroze(data, conn, table="Podroze"):
    cur = conn.cursor()
    for row in data:
        pod_row = PodrozeRow(row)
        cols = pod_row.items.keys()
        vals = [pod_row.items[col] for col in cols]
        cur.execute(cur.mogrify(f"INSERT INTO {table}(%s) VALUES %s", ((AsIs(', '.join(cols))), tuple(vals))))
        conn.commit()
    cur.close()

# INSERT INTO tabela('Nazwa')