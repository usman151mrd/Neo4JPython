import datetime

from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import *
from Functions.functions import *
from TNodeWrapper import Neo4jNode


class Neo4jRelation:
    def __init__(self, _relation=None):
        self.__relation = _relation
        self.db = Neo4Niha()

    def set_relation(self, value):
        self.__relation = value

    def create_query(self):
        print(self.__relation.SourceNode)
        print(self.__relation.TargetNode)
        query1 = "MERGE (n"
        for label in self.__relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.__relation.SourceNode.AoKID + ", Value:" + self.__relation.SourceNode.Value + ", SystemLevelType:'" + self.__relation.SourceNode.SystemLevelType + "', AbstractionLevel:'" + self.__relation.SourceNode.AbstractionLevel + "', Tag:'" + self.__relation.SourceNode.Tag + "', Validity:'" + self.__relation.SourceNode.Validity + "', ProcessingTag:'" + self.__relation.SourceNode.ProcessingTag + "', Evaluation:'" + self.__relation.SourceNode.Evaluation + "', AgeInMilliseconds:'" + self.__relation.SourceNode.AgeInMilliseconds + "', AttentionLevel:'" + self.__relation.SourceNode.AttentionLevel + "'"
        if self.__relation.SourceNode.TruthValue is not None:
            for key, value in zip(self.__relation.SourceNode.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query1 += ", TV_" + key + ":" + value
        query1 += "})"

        query2 = " MERGE (m"
        for label in self.__relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + self.__relation.TargetNode.AoKID + ", Value:" + self.__relation.TargetNode.Value + ", SystemLevelType:'" + self.__relation.TargetNode.SystemLevelType + "', AbstractionLevel:'" + self.__relation.TargetNode.AbstractionLevel + "', Tag:'" + self.__relation.TargetNode.Tag + "', Validity:'" + self.__relation.TargetNode.Validity + "', ProcessingTag:'" + self.__relation.TargetNode.ProcessingTag + "', Evaluation:'" + self.__relation.TargetNode.Evaluation + "', AgeInMilliseconds:'" + self.__relation.TargetNode.AgeInMilliseconds + "', AttentionLevel:'" + self.__relation.TargetNode.AttentionLevel + "'"
        if self.__relation.TargetNode.TruthValue is not None:
            for key, value in zip(self.__relation.TruthValue.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query2 += ", TV_" + key + ":" + value
        query2 += "})"
        return query1 + query2 + " Merge (n)-[r:" + self.__relation.RelationType + " {AoKID:'" + self.__relation.AoKID + "', RelationType:'" + self.__relation.RelationType + "', AttentionLevel: '" + self.__relation.AttentionLevel + "'}]-(m) return ID(n) as sid,ID(r) as rid,ID(m) as tid"

    def update_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " set r.AoKID= " + self.__relation.AoKID + ", r.RelationType= '" + self.__relation.RelationType + "', r.IsBiDirectional= '" + self.__relation.IsBiDirectional + "' ,r.AttentionLevel= '" + self.__relation.AttentionLevel + "' return r"

    def retrieve_query(self, r_id):
        return "match (s)-[r]-(t) where ID(r)=" + r_id + " return s,r,t"

    def delete_relation_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " delete r"

    def create_relation(self):
        query = self.create_query()
        print(query)
        response = self.db.create(query)
        _id_dictionary = [{"sid": record['sid'], "rid": record['rid'], "tid": record['tid']}
                          for record in response]
        return _id_dictionary
        # update logic here because graph is already generated on just assign neo4j id
        # ids after generated graph physically

    def retrieve_relation(self, r_id):
        query = self.retrieve_query(r_id)
        response = self.db.retrieve(query)
        return to_graph(response)

    def delete_relation(self, r_id):
        query = self.delete_relation_query(r_id)
        response = self.db.delete(query)

    def update_relation(self, r_id):
        query = self.update_query(r_id)
        print(query)
        response = self.db.update(query)
        return to_graph(response)

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
