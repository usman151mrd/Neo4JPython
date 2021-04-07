import json


def load_config():
    with open("../Functions/config.json") as json_data_file:
        data = json.load(json_data_file)
    conf = data["neo4j"]
    scheme = conf["scheme"]
    host = conf["host"]
    port = conf["port"]
    user = conf["user"]
    password = conf["password"]
    url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host, port=port)
    return url, user, password
