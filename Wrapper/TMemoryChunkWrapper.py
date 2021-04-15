from Functions.functions import to_graph
from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import TNode, TRelation, TGraph, TMemoryChunk
from Wrapper.TGraphWrapper import Neo4jGraph
from Wrapper.TRelationWrapper import Neo4jRelation


class Neo4jMemoryChunk:
    def __init__(self, _memory_chunk=None):
        self.memory_chunk = _memory_chunk
        self.db = Neo4Niha()
        self.__relation = TRelation
        self.__graph = Neo4jGraph

    def set_memoryChunk(self, value):
        self.memory_chunk = value

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
        self.__graph.ID = response[0]['id']

    def retrieve_memory_chunk(self, _id):
        q = "match (m:MemoryChunk) where ID(m)={0} return m".format(_id)
        response = self.db.retrieve(q)
        properties = response[0].data()
        gid = properties['m']['gid']
        self.memory_chunk.Graph = self.__graph.retrieve_by_id(gid)
        self.memory_chunk.Capacity = properties['m']['Capacity']
        self.memory_chunk.TimeStamp = properties['m']['TimeStamp']
        self.memory_chunk.DecayLevel = properties['m']['DecayLevel']
        self.memory_chunk.AttentionLevel = properties['m']['AttentionLevel']
        self.memory_chunk.Evaluation = properties['m']['Evaluation']
        self.memory_chunk.Importance = properties['m']['Importance']

    def update_memory_chunk(self, _id):
        query = "MATCH (n:MemoryChunk where ID(m)={0} set TimeStamp={1}, Capacity={2},A ttentionLevel:{3}," \
                "DecayLevel:{4},Importance:{5},Evaluation:{6}) return 1".format(
            _id, self.memory_chunk.TimeStamp, self.memory_chunk.Capacity, self.memory_chunk.AttentionLevel,
            self.memory_chunk.DecayLevel, self.memory_chunk.Importance,
            self.memory_chunk.Evaluation)
        response = self.db.update(query)

    def delete_memory_chunk(self, _id):
        q = "match (m:MemoryChunk) where ID(m)={0} DETACH DELETE m return 1".format(_id)
        response = self.db.delete(q)

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
