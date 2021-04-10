from Neo4JLayer.Neo4j import Neo4Niha
from Node import Node
from Functions.functions import to_tnode
import datetime

from niha_thrift.ttypes import TNode


class Neo4jNode:
    def __init__(self, node):
        self.node = node
        self.db = Neo4Niha()

    def create_node_query(self):
        query = "CREATE (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += " {AoKID:" + self.node.AoKID + ", Value:" + self.node.Value + ", SystemLevelType:'" + self.node.SystemLevelType + "', AbstractionLevel:'" + self.node.AbstractionLevel + "', Tag:'" + self.node.Tag + "', Validity:'" + self.node.Validity + "', ProcessingTag:'" + self.node.ProcessingTag + "', Evaluation:'" + self.node.Evaluation + "', DateTimeStamp:'" + self.node.DateTimeStamp + "', AgeInMilliseconds:'" + self.node.AgeInMilliseconds + "', AttentionLevel:'" + self.node.AttentionLevel + "', TV_keys: "+str(list(self.node.TruthValue.keys()))
        if self.node.TruthValue is not None:
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ", " + key + ":" + value
        query += "}) RETURN ID(n) as id"
        return query

    def delete_node_query(self, n_id):
        return "match (n) where ID(n)=" + n_id + " detach delete n return 1"

    def retrieve_node_query(self, n_id):
        return "match (n) where ID(n)=" + n_id + " return n"

    def update_node_query(self, n_id):
        query = "MATCH (n) where ID(n)=" + n_id + " SET "
        query += " n.AoKID=" + self.node.AoKID + ", n.Value=" + self.node.Value + ", n.SystemLevelType='" + self.node.SystemLevelType + "', n.AbstractionLevel='" + self.node.AbstractionLevel + "', n.Tag='" + self.node.Tag + "', n.Validity='" + self.node.Validity + "', n.ProcessingTag='" + self.node.ProcessingTag + "', n.Evaluation='" + self.node.Evaluation + "', n.DateTimeStamp='" + self.node.DateTimeStamp + "', n.AgeInMilliseconds='" + self.node.AgeInMilliseconds + "', n.AttentionLevel='" + self.node.AttentionLevel + "', n.TV_keys= "+str(list(self.node.TruthValue.keys()))
        if self.node.TruthValue is not None:
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ", n." + key + "=" + value
        query += " return 1"
        return query

    def create_node(self):
        query = self.create_node_query()
        print(query)
        response = self.db.create(query)
        self.node.Neo4jID = response[0]
        return self.node.Neo4jID

    def retrieve_node(self, n_id):
        query = self.retrieve_node_query(n_id)
        response = self.db.retrieve(query)
        _nodes = (to_tnode(response[0]['n']))
        return _nodes

    def delete_node(self, n_id):
        query = self.delete_node_query(n_id)
        response = self.db.delete(query)


    def update_node(self, n_id):
        query = self.update_node_query(n_id)
        response = self.db.update(query)

if __name__ == '__main__':
    node1=TNode(AoKID='1',Labels={"person2"},Value="4",SystemLevelType="abc",AbstractionLevel="first", Tag="abc", Validity="val",ProcessingTag="ptag",TruthValue={'Key1':'1234','Key2':'125'}, Evaluation="aaa",DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700")
    neo4=Neo4jNode(node1)
    nod=neo4.create_node()
    print(nod)
    #nod=neo4.retrieve_node("70")
    #print(nod)
    #nod=neo4.update_node("70")
    #print(nod)
    #nod=neo4.delete_node("70")