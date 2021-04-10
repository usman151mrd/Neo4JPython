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
        query += " {AoKID:" + self.node.AoKID + ", Value:" + self.node.Value + ", SystemLevelType:" + self.node.SystemLevelType + ", AbstractionLevel:" + self.node.AbstractionLevel + ", Tag:" + self.node.Tag + ", Validity:" + self.node.Validity + ", ProcessingTag:" + self.node.ProcessingTag + ", Evaluation:" + self.node.Evaluation + ", DateTimeStamp:" + self.node.DateTimeStamp + ", AgeInMilliseconds:" + self.node.AgeInMilliseconds + ", AttentionLevel:" + self.node.AttentionLevel
        if self.node.TruthValue!=None:
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ", TV_" + key + ":" + value
        query += "}) RETURN ID(n) as id"
        #print(query)
        return query

    def delete_node_query(self, n_id):
        return "match (n) where ID(n)=" + n_id + " detach delete n"

    def retrieve_node_query(self, n_id):
        return "match (n) where ID(n)=" + n_id + " return n"

    def update_node_query(self, n_id):
        query = "MATCH (n) where ID(n)=" + n_id + " SET "
        query += " n.AoKID=" + self.node.AoKID + ", n.Value=" + self.node.Value + ", n.SystemLevelType='" + self.node.SystemLevelType + "', n.AbstractionLevel='" + self.node.AbstractionLevel + "', n.Tag='" + self.node.Tag + "', n.Validity='" + self.node.Validity + "', n.ProcessingTag='" + self.node.ProcessingTag + "', n.Evaluation='" + self.node.Evaluation + "', n.DateTimeStamp='" + self.node.DateTimeStamp + "', n.AgeInMilliseconds='" + self.node.AgeInMilliseconds + "', n.AttentionLevel='" + self.node.AttentionLevel+ "'"
        if self.node.TruthValue!=None:
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ", n.TV_" + key + "=" + value
        query += "return n"
        return query

    def create_node(self):
        query = self.create_node_query()
        response = self.db.create(query)
        self.node.Neo4jID = response[0]



    def retrieve_node(self, n_id):
        _nodes = []
        query = self.retrieve_node_query(n_id)
        response = self.db.retrieve(query)
        for node_ in response:
            _nodes.append(to_tnode(node_['n']))
        return _nodes

    def delete_node(self, n_id):
        query = self.delete_node_query(n_id)
        #query = "MATCH (n:Laptop) DETACH DELETE n"
        response = self.db.delete(query)

    def update_node(self, n_id):
        query = self.update_node_query(n_id)
        response = self.db.update(query)
        return self.to_tnode(response)

    # def to_tnode(self, response):
    #     tnode1 = TNode()
    #
    #     for node in response:
    #         data = node.data()
    #         tnode1.Labels = set(node['n'].labels)
    #         tnode1.Id = node['n'].id
    #         tnode1.Labels = set(node['n'].labels)
    #         tnode1.Id = node['n'].id
    #         tnode1.AoKID = data['n']['AoKID']
    #         tnode1.AbstractionLevel = data['n']['AbstractionLevel']
    #         tnode1.AgeInMilliseconds = data['n']['AgeInMilliseconds']
    #         tnode1.AttentionLevel = data['n']['AttentionLevel']
    #         tnode1.Value = data['n']['Value']
    #         tnode1.Validity = data['n']['Validity']
    #         tnode1.Tag = data['n']['Tag']
    #         tnode1.Evaluation = data['n']['Evaluation']
    #         tnode1.ProcessingTag = data['n']['ProcessingTag']
    #         tnode1.SystemLevelType = data['n']['SystemLevelType']
    #         #tnode1.TruthValue = data['n']['TruthValue']
    #     return tnode1


if __name__ == '__main__':
    node = TNode(AoKID="1", Labels={"Tester2"}, Value="1", SystemLevelType="abc", AbstractionLevel="1", Tag="Abs", Validity="not > 20", ProcessingTag="ptag", Evaluation="123", DateTimeStamp=str(datetime.datetime.now()), AgeInMilliseconds="600", AttentionLevel="1")
    tnode = Neo4jNode(node)
    nod=tnode.create_node()
    nod=tnode.retrieve_node("1")
    nod=tnode.update_node("1")
    tnode.delete_node("1")
    print(nod.Labels)
    def __init__(self, Neo4jID=None, AoKID=None, Labels=None, Value=None, SystemLevelType=None, AbstractionLevel=None, Tag=None, Validity=None, ProcessingTag=None, TruthValue=None, Evaluation=None, DateTimeStamp=None, AgeInMilliseconds=None, AttentionLevel=None,):
