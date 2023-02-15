from configparser import ConfigParser

REQUEST_TIMEOUT = 30
REGEX_TIMEOUT   = 7

KAFKA_TOPIC = "web_monitorial"

URLS = [
        {"name":"Google", "url":"https://google.com", "interval":30, "pattern":"div"},
        {"name":"StackOverFlow","url":"https://stackoverflow.com/", "interval":10},
        {"name":"Aiven","url":"https://aiven.io/", "interval":10, "pattern":"salam"},
        ]


def config(filename='env.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

