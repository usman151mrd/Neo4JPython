from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from TGraphWrapper import Neo4jGraph
from Relation import Relation
from Node import Node
from TRelationWrapper import Neo4jRelation
from MemoryChunk import MemoryChunk


class Neo4jMemoryChunk:
    def __init__(self, memorychunk):
        self.memorychunk = memorychunk
        self.db = Neo4Niha()

    def create_memorychunk(self):
        graph = Graph()
        relation = Relation()
        trelation = Neo4jRelation(relation)
        response = trelation.create_relation()
        neo4graph = Neo4jGraph(graph)
        neo4graph.to_graph(response)
        self.to_memorychunck(graph)

    def retrieve_memorychunk(self):
        graph = Graph()
        neo4graph = Neo4jGraph(graph)
        neo4graph.retrieve_graph()
        self.to_memorychunck(graph)

    def update_memorychunk(self):
        pass

    def delete_memorychunk(self):
        pass

    def to_memorychunck(self, neo4graph):
        memorychunk = MemoryChunk()
        memorychunk.Graph = neo4graph
        # memorychunk.type="graph"
        memorychunk.Nid = neo4graph.Nodes
        memorychunk.Rid = neo4graph.Relation
        memorychunk.rtype = neo4graph.Relation['relation']
