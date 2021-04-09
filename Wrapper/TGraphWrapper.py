from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from niha_thrift.ttypes import TGraph


class Neo4jGraph:
    def __init__(self, graph):
        self.graph = graph
        self.db = Neo4Niha()

    def retrieve_graph(self):
        query = "MATCH (m:TEST3)-[r:isA]->(n:TEST4) RETURN m,r,n LIMIT 25"
        response = self.db.retrieve(query)
        self.to_graph(response)
        return self.graph

    def create_graph(self):
        pass


if __name__ == '__main__':
    g = Graph()
    n4j = Neo4jGraph(g)
    n4j.retrieve_graph()
    print("nodes : ", g.Nodes)
    print("edges : ", g.Relation)
