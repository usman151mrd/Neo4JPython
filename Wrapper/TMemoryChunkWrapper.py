from Functions.functions import to_graph
from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import TNode, TRelation, TGraph, TMemoryChunk
from TGraphWrapper import Neo4jGraph
from TRelationWrapper import Neo4jRelation


class Neo4jMemoryChunk:
    def __init__(self, memory_chunk):
        self.memory_chunk = memory_chunk
        self.db = Neo4Niha()
        self.__relation = TRelation
        self.__graph = Neo4jGraph

    def set_memory_chunk(self, memory_chunk):
        self.memory_chunk = memory_chunk

    def create_memory_chunk(self):
        self.__graph.graph = self.memory_chunk.Graph
        self.__graph.create_graph()
        query = "create (n:MemoryChunk {name:'MemoryChunk',TimeStamp:'" \
                + self.memory_chunk.TimeStamp + "',Capacity:" + self.memory_chunk.Capacity + ", "
        query += "AttentionLevel:{0},DecayLevel:{1},Importance:{2},Evaluation:{3},gid:{4}) return ID(n) as id ".format(
            self.memory_chunk.AttentionLevel, self.memory_chunk.DecayLevel, self.memory_chunk.Importance,
            self.memory_chunk.Evaluation, self.memory_chunk.Graph.Neo4jID)
        response = self.db.create(query)
        self.graph.ID = response[0]['id']

    def retrieve_memory_chunk(self, _id):
        graph = TGraph()
        neo4graph = Neo4jGraph(graph)
        neo4graph.retrieve_by_id()
        self.to_memorychunck(graph)

    def update_memory_chunk(self):
        pass

    def delete_memory_chunk(self):
        pass

    def to_memory_chunck(self, neo4graph):
        memory_chunk = TMemoryChunk()
        memory_chunk.Graph = neo4graph
        memory_chunk.Nid = neo4graph.Nodes
        memory_chunk.Rid = neo4graph.Relation
        memory_chunk.rtype = neo4graph.Relation['_relation']

    def retrieve_by_id(self, _id):
        q = "match (m) where ID(g)={0} return m".format(_id)
        response = self.db.retrieve(q)
        properties = response[0].data()
        print(properties)


if __name__ == '__main__':
    memory_ = TMemoryChunk()
    memory = Neo4jMemoryChunk(memory_)
    memory.retrieve_by_id()
