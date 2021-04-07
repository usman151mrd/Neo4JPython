from neo4j import GraphDatabase, basic_auth
import json


class DataBase:

    def __init__(self):
        url, user, password = load_config()
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        self.driver.close()

    def write(self, query):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.create, query)
            print(greeting)

    @staticmethod
    def create(tx, query):
        result = tx.run(query)
        print("Response : ", result.single()[0])
        return result

    def retrieve(self, name):
        with self.driver.session() as session:
            return session.read_transaction(self.get_tags, name)

    @staticmethod
    def get_tags(tx, name):
        query = "MATCH (n)-[r:isA]->(m) where n.name=$name return m.name as name"
        result = tx.run(query, name=name)
        tags = [node for node in result]
        return tags

