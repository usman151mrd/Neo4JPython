from Neo4JLayer.Neo4j import Neo4Niha
# from Node import Node
from Functions.functions import to_tnode
import datetime

from niha_thrift.ttypes import TNode


class Neo4jNode:
    def __init__(self, _node=None):
        self.node = _node
        self.db = Neo4Niha()

    def set_node(self, value):
        self.node = value

    def create_node_query(self):
        query = "CREATE (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += " {"
        query += "AoKID:{0} , Value:{1}, SystemLevelType:{2} , AbstractionLevel:{3}, Tag:'{4}', Validity:'{5}', " \
                 "ProcessingTag:'{6}', Evaluation:{7}, AgeInMilliseconds:{8}, AttentionLevel:{9}, Domains:{10}".format(
            self.node.AoKID, self.node.Value,
            self.node.SystemLevelType, self.node.AbstractionLevel,
            self.node.Tag, self.node.Validity,
            self.node.ProcessingTag, self.node.Evaluation,
            self.node.AgeInMilliseconds, self.node.AttentionLevel, list(self.node.Domains))
        # for domain in self.node.Domains:
        #     query += "{domain},".format(domain=domain)

        if self.node.TruthValue is not None:
            Keylis=[]
            for key in self.node.TruthValue.keys():
                Keylis.append(key)
            query += ", Keys:{0}".format(list(Keylis))
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                query += ",{0} :{1}".format(key, value)

        query += "}) RETURN ID(n) as id"
        print(query)
        return query

    def delete_node_query(self, n_id):
        return "match (n) where ID(n)={0} detach delete n return 1".format(n_id)

    def retrieve_node_query(self, n_id):
        return "match (n) where ID(n)={0} return n".format(n_id)

    def update_node_query(self, n_id):
        query = "MATCH (n) where ID(n)=" + n_id + " SET "
        query += "n.AoKID={0} , n.Value={1}, n.SystemLevelType={2} , n.AbstractionLevel={3}, n.Tag='{4}', n.Validity='{5}', " \
                 "n.ProcessingTag='{6}', n.Evaluation={7}, n.AgeInMilliseconds={8}, n.AttentionLevel={9}, n.Domains={10}".format(
            self.node.AoKID, self.node.Value,
            self.node.SystemLevelType, self.node.AbstractionLevel,
            self.node.Tag, self.node.Validity,
            self.node.ProcessingTag, self.node.Evaluation,
            self.node.AgeInMilliseconds, self.node.AttentionLevel, list(self.node.Domains))
        if self.node.TruthValue is not None:
            Keylis = []
            for key in self.node.TruthValue.keys():
                Keylis.append(key)
            query += ", n.Keys={0}".format(list(Keylis))
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ",n.{0} ={1}".format(key, value)
                #query += ", n." + key + "=" + value
        query += " return 1"
        return query

    def create_node(self):
        query = self.create_node_query()
        response = self.db.create(query)
        self.node.Neo4jID = response[0]
        _id=""
        for record in response:
            _id=record['id']
        return str(_id)

    def retrieve_node(self, n_id):
        query = self.retrieve_node_query(n_id)
        response = self.db.retrieve(query)
        node=to_tnode(response[0]['n'])
        print(node)
        return node

    def delete_node(self, n_id):
        query = self.delete_node_query(n_id)
        response = self.db.delete(query)
        if response==1:
            return True
        else:
            return False

    def update_node(self, n_id):
        query = self.update_node_query(n_id)
        #print(query)
        response = self.db.update(query)
        print(response)
        if response == '1':
            return True
        else:
            return False


if __name__ == '__main__':
    node1 = TNode(AoKID='1', Labels={"person2"}, Value="4", SystemLevelType="abc", AbstractionLevel="first", Tag="abc",
                  Validity="val", ProcessingTag="ptag", TruthValue={'Key1': '1234', 'Key2': '125'}, Evaluation="aaa",
                  DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700", Domains={"Human", "Living"})
    neo4 = Neo4jNode(node1)
    nod = neo4.create_node()
    print(nod)
    # nod=neo4.retrieve_node("70")
    # print(nod)
    # nod=neo4.update_node("70")
    # print(nod)
    # nod=neo4.delete_node("70")
