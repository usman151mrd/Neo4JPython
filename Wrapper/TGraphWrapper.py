from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from niha_thrift.ttypes import TGraph
from TRelationWrapper import Neo4jRelation

from Functions.functions import *


class Neo4jGraph:
    def __init__(self, graph):
        self.graph = graph
        self.db = Neo4Niha()
        self.__relation = Neo4jRelation()

    def retrieve_graph(self):
        query = "MATCH (m)-[r:KNOWS]->(n) RETURN m,r,n LIMIT 25"
        response = self.db.retrieve(query)
        self.graph = to_graph(response)
        return self.graph

    def create_graph(self):
        _node_ids = set()
        _edge_ids = set()
        for _rel in self.graph.Edges:
            self.__relation.set_relation(_rel)
            _ids = self.__relation.create_relation()
            sid, rid, tid = _ids[0]['sid'], _ids[0]['rid'], _ids[0]['tid']
            _rel.SourceNode.Neo4jID = sid
            _rel.TargetNode.Neo4jID = tid
            _rel.Neo4jID = rid
            _node_ids.update([sid, tid])
            _edge_ids.add(rid)
        query = "create (g:Graph {name:'graph',nid:" + str(list(_node_ids)) + ",rid:" + str(list(
            _edge_ids)) + "}) return ID(g) as id"
        self.db.create(query)


if __name__ == '__main__':
    # Nlist=[]
    # Rlist=[]
    # node1=TNode(AoKID='1',Labels={"person1"},Value="4",SystemLevelType="abc",AbstractionLevel="first", Tag="abc", Validity="val",ProcessingTag="ptag",TruthValue={'Key1':'1234','Key2':'125'}, Evaluation="aaa",DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700")
    # node2=TNode(AoKID='2',Labels={"person2"},Value="4",SystemLevelType="abc",AbstractionLevel="first", Tag="abc", Validity="val",ProcessingTag="ptag",TruthValue={'Key1':'1234','Key2':'125'}, Evaluation="aaa",DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700")
    # node3=TNode(AoKID='3',Labels={"person3"},Value="4",SystemLevelType="abc",AbstractionLevel="first", Tag="abc", Validity="val",ProcessingTag="ptag",TruthValue={'Key1':'1234','Key2':'125'}, Evaluation="aaa",DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700")
    # Nlist.append(node1)
    # Nlist.append(node2)
    # Nlist.append(node3)
    # rel1=TRelation(AoKID='4', Labels={"knows"},RelationType="KNOWS",SourceNode=node1,TargetNode=node2,Properties="abc",AttentionLevel="alevel",TruthValue={'RKey1':'1234','RKey2':'125'})
    # rel2=TRelation(AoKID='5', Labels={"Dontknows"},RelationType="DONTKNOWS",SourceNode=node1,TargetNode=node3,Properties="abc",AttentionLevel="alevel",TruthValue={'RKey1':'1234','RKey2':'125'})
    # Rlist.append(rel1)
    # Rlist.append(rel2)
    # g = TGraph(Nodes=Nlist,Edges=Rlist)
    g = TGraph()
    n4j = Neo4jGraph(g)
    # n4j.create_graph()
    g = n4j.retrieve_graph()
    print("nodes : ", g.Nodes)
    print("edges : ", g.Relation)
