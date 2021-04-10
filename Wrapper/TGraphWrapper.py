from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from niha_thrift.ttypes import TGraph
from TRelationWrapper import Neo4jRelation

from Functions.functions import *
class Neo4jGraph:
    def __init__(self, graph):
        self.graph = graph
        self.db = Neo4Niha()
        self.__relation = Neo4jRelation

    def retrieve_graph(self):
        query = "MATCH (m:TEST3)-[r:isA]->(n:TEST4) RETURN m,r,n LIMIT 25"
        response = self.db.retrieve(query)
        to_graph(response)
        return self.graph

    def create_graph(self):
        _node_ids = set()
        _edge_ids = set()
        for _rel in self.graph.Relation:
            self.__relation.set_relation(_rel)
            _ids = self.__relation.create_relation()
            sid, rid, tid = _ids['sid'], _ids['rid'], _ids['tid']
            _rel.SourceNode.Neo4jID = sid
            _rel.TargetNode.Neo4jID = tid
            _rel.Neo4jID = rid
            _node_ids.update([sid, tid])
            _edge_ids.add(rid)
        query = "create (g:Graph {name:'graph',nid:"+list(_node_ids)+",rid:"+list(_edge_ids)+"}) return ID(g) as id"
        self.db.create(query)


if __name__ == '__main__':
    g = Graph()
    n4j = Neo4jGraph(g)
    n4j.retrieve_graph()
    print("nodes : ", g.Nodes)
    print("edges : ", g.Relation)
