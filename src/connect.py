import psycopg2


def get_connection(params):
    return psycopg2.connect(**params)
