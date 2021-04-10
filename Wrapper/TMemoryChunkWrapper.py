from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from TGraphWrapper import Neo4jGraph
from Relation import Relation
from Node import Node
from TRelationWrapper import Neo4jRelation
from MemoryChunk import MemoryChunk


class Neo4jMemoryChunk:
    def __init__(self, memory_chunk):
        self.memory_chunk = memory_chunk
        self.db = Neo4Niha()
        self.graph = Relation

    def create_query(self):
        nodes = []
        edges = []
        for node in self.memory_chunk.Graph.Nodes:
            nodes.append(node.Id)
        for edge in self.memory_chunk.Graph.Relation:
            edges.append(edge.Neo4jID)
        query = "create (n:Graph {name:'Graph',nid:" + nodes + ",rid:" + edges + ",TimeStamp:'" \
                + self.memory_chunk.TimeStamp + "',Capacity:" + self.memory_chunk.Capacity + ", "
        query += "AttentionLevel:{0},DecayLevel:{1},Importance:{2},Evaluation:{3}) return ID(n) ".format(
            self.memory_chunk.AttentionLevel, self.memory_chunk.DecayLevel, self.memory_chunk.Importance,
            self.memory_chunk.Evaluation)

    def create_memory_chunk(self):
        graph = self.memory_chunk.Graph

    def retrieve_memory_chunk(self):
        graph = Graph()
        neo4graph = Neo4jGraph(graph)
        neo4graph.retrieve_graph()
        self.to_memorychunck(graph)

    def update_memory_chunk(self):
        pass

    def delete_memory_chunk(self):
        pass

    def to_memory_chunck(self, neo4graph):
        memorychunk = MemoryChunk()
        memorychunk.Graph = neo4graph
        # memorychunk.type="graph"
        memorychunk.Nid = neo4graph.Nodes
        memorychunk.Rid = neo4graph.Relation
        memorychunk.rtype = neo4graph.Relation['_relation']
