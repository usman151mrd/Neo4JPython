import datetime

from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import *
from Functions.functions import *
from Wrapper.TNodeWrapper import Neo4jNode


class Neo4jRelation:
    def __init__(self, _relation=None):
        self.__relation = _relation
        self.db = Neo4Niha()

    def set_relation(self, value):
        self.__relation = value

    def create_query(self):
        query1 = "MERGE (n"
        for label in self.__relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {"
        query1 += "AoKID:{0} , Value:{1}, SystemLevelType:{2} , AbstractionLevel:{3}, Tag:'{4}', Validity:'{5}', " \
                  "ProcessingTag:'{6}', Evaluation:{7}, AgeInMilliseconds:{8}, AttentionLevel:{9}, Domains:{10}".format(
            self.__relation.SourceNode.AoKID, self.__relation.SourceNode.Value,
            self.__relation.SourceNode.SystemLevelType, self.__relation.SourceNode.AbstractionLevel,
            self.__relation.SourceNode.Tag, self.__relation.SourceNode.Validity,
            self.__relation.SourceNode.ProcessingTag, self.__relation.SourceNode.Evaluation,
            self.__relation.SourceNode.AgeInMilliseconds, self.__relation.SourceNode.AttentionLevel,
            list(self.__relation.SourceNode.Domains))
        if self.__relation.SourceNode.TruthValue is not None:
            Keylis = []
            for key in self.__relation.TargetNode.TruthValue.keys():
                Keylis.append(key)
            query1 += ", Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.SourceNode.TruthValue.keys(),
                                  self.__relation.SourceNode.TruthValue.values()):
                # print(key, value)
                query1 += ", {0} :{1}".format(key, value)
        query1 += "})"

        query2 = " MERGE (m"
        for label in self.__relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {"
        query2 += "AoKID:{0} , Value:{1}, SystemLevelType:{2} , AbstractionLevel:{3}, Tag:'{4}', Validity:'{5}', " \
                  "ProcessingTag:'{6}', Evaluation:{7}, AgeInMilliseconds:{8}, AttentionLevel:{9}, Domains:{10}".format(
            self.__relation.TargetNode.AoKID, self.__relation.TargetNode.Value,
            self.__relation.TargetNode.SystemLevelType, self.__relation.TargetNode.AbstractionLevel,
            self.__relation.TargetNode.Tag, self.__relation.TargetNode.Validity,
            self.__relation.TargetNode.ProcessingTag, self.__relation.TargetNode.Evaluation,
            self.__relation.TargetNode.AgeInMilliseconds, self.__relation.TargetNode.AttentionLevel,
            list(self.__relation.TargetNode.Domains))
        if self.__relation.TargetNode.TruthValue is not None:
            Keylis = []
            for key in self.__relation.TargetNode.TruthValue.keys():
                Keylis.append(key)
            query2 += ", Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TargetNode.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query2 += ", {0} : {1}".format(key, value)
        query2 += "})"
        query = query1 + query2 + "Merge (n)-[r"
        for label in self.__relation.Labels:
            query += ":{label}".format(label=label)
        query += "{"
        query += "AoKID:{0}, RelationType:'{1}', AttentionLevel:{2} ,IsBiDirectional:{3}".format(self.__relation.AoKID,
                                                                                                 self.__relation.RelationType,
                                                                                                 self.__relation.AttentionLevel,
                                                                                                 self.__relation.IsBiDirectional)
        if self.__relation.TruthValue is not None:
            Keylis = []
            for key in self.__relation.TruthValue.keys():
                Keylis.append(key)
            query += ", Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TruthValue.keys(), self.__relation.TruthValue.values()):
                query += ",{0} :{1}".format(key, value)
        query += "}]-(m) return ID(n) as sid,ID(r) as rid,ID(m) as tid"
        return query

    def update_query(self, r_id):
        query = "match ()-[r]-() where ID(r)={0} set r.AoKID={1}, r.RelationType='{2}'" \
                ", r.AttentionLevel={3} ".format(
            r_id, self.__relation.AoKID, self.__relation.RelationType, self.__relation.AttentionLevel)
        if self.__relation.TruthValue is not None:
            keylis = []
            for key in self.__relation.TruthValue.keys():
                keylis.append(key)
            query += ", r.Keys={0}".format(list(keylis))
            for key, value in zip(self.__relation.TruthValue.keys(), self.__relation.TruthValue.values()):
                query += ",r.{0} ={1}".format(key, value)

        query += " return 1"
        return query

    def retrieve_query(self, r_id):
        return "match (s)-[r]-(t) where ID(r)={0} return s,r,t".format(r_id)

    def delete_relation_query(self, r_id):
        return "match ()-[r]-() where ID(r)={0} delete r".format(r_id)

    def create_relation(self):
        query = self.create_query()
        response = self.db.create(query)
        _id_dictionary = [{"sid": record['sid'], "rid": record['rid'], "tid": record['tid']}
                          for record in response]
        return _id_dictionary
        # update logic here because graph is already generated on just assign neo4j id
        # ids after generated graph physically

    def retrieve_relation(self, r_id):
        query = self.retrieve_query(r_id)
        response = self.db.retrieve(query)
        relation=None
        for node in response:
            source_node = to_tnode(node['r'].nodes[0])
            target_node = to_tnode(node['r'].nodes[1])
            _id = node['r'].id
            _type = node['r'].type
            properties = dict(node['r'])
            relation = to_relation(_id, source_node, target_node, _type, properties)
        return relation

    def delete_relation(self, r_id):
        query = self.delete_relation_query(r_id)
        response = self.db.delete(query)
        return response

    def update_relation(self, r_id):
        query = self.update_query(r_id)
        print(query)
        response = self.db.update(query)
        return response

    def retrieve_by_id(self, _id):
        query = "match (m)-[r]-(n) where ID(r)={0} return m,r,n".format(_id)
        return self.db.retrieve(query)


if __name__ == '__main__':
    node = TNode(AoKID="1", Labels={"Tester"}, Value="1", SystemLevelType="abc", AbstractionLevel="1", Tag="Abs",
                 Validity="not > 20", ProcessingTag="ptag", Evaluation="123",
                 DateTimeStamp=str(datetime.datetime.now()), AgeInMilliseconds="600", AttentionLevel="1")
    tnode = Neo4jNode(node)
    # nod = tnode.create_node()
    SourceNode = tnode.retrieve_node("32")
    # print("source",SourceNode)
    TargetNode = tnode.retrieve_node("1")
    # print("target",TargetNode)
    relation = TRelation(AoKID="25", Labels={"trial"}, RelationType="trial", SourceNode=SourceNode,
                         TargetNode=TargetNode,
                         IsBiDirectional="True", AttentionLevel="3")
    trelation = Neo4jRelation(relation)
    trelation.create_relation()
    # trelation.retrieve_relation("53")
    # trelation.update_relation("53")
    # trelation.delete_relation("53")
    # def __init__(self, Neo4jID=None, AoKID=None, Labels=None, RelationType=None, SourceNode=None, TargetNode=None, IsBiDirectional=None, Properties=None, AttentionLevel=None, TruthValue=None,):
