from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import TGraph
from Wrapper.TRelationWrapper import Neo4jRelation

from Functions.functions import *


class Neo4jGraph:
    def __init__(self, _graph=None):
        self.graph=_graph
        self.db = Neo4Niha()
        self.__relation = Neo4jRelation()

    def set_graph(self, value):
        self.graph = value
        print(value)

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
        query = "create (g:Graph {name:'graph',nid:{0},rid:{1}) return ID(g) as id".format(
            list(_node_ids), list(_edge_ids))
        response = self.db.create(query)

    def update_query(self, g_id):
        q = "match (g:Graph) where ID(g)={0} set g.nid= {1}, g.rid={2} return 1".format(g_id,list(self.graph.Nodes), list(self.graph.Edges))

    def delete_query(self, g_id):
        q = "match (g:Graph) where ID(g)={0} DETACH DELETE g RETURN 1".format(g_id)
        response = self.db.delete(q)

    def retrieve_by_id(self, _id):
        q = "match (g:Graph) where ID(g)={0} return g".format(_id)
        response = self.db.retrieve(q)
        properties = response[0].data()
        rel = []
        for rid in properties['g']['rid']:
            r = self.__relation.retrieve_by_id(rid)
            rel += r
        _graph = to_graph(rel)
        _graph.ID = response[0]['g'].id
        self.graph = _graph
        return _graph


if __name__ == '__main__':
    g = TGraph()
    n4j = Neo4jGraph(g)
    # n4j.retrieve_graph()
    n4j.retrieve_by_id(76)
    # print("nodes : ", g.Nodes)
    # print("edges : ", g.Relation)
