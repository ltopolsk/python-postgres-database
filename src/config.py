from configparser import ConfigParser, NoSectionError


def config(filename='database.ini', section='postgresql'):
    try:
        parser = ConfigParser()
        parser.read(filename)
        database = {}
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]
    except FileNotFoundError as e:
        raise e
    except NoSectionError:
        raise Exception(f'section {section} not found in the file {filename}')

    return database


if __name__ == "__main__":
    print(config())
