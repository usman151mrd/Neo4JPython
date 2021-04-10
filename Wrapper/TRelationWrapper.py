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
        print(self.__relation)
        query1 = "MERGE (n"
        for label in self.__relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID: " + str(self.__relation.SourceNode.AoKID) + ", Value: " + str(self.__relation.SourceNode.Value) + ", SystemLevelType:'" + self.__relation.SourceNode.SystemLevelType + "', AbstractionLevel:'" + self.__relation.SourceNode.AbstractionLevel + "', Tag:'" + self.__relation.SourceNode.Tag + "', Validity:'" + self.__relation.SourceNode.Validity + "', ProcessingTag:'" + self.__relation.SourceNode.ProcessingTag + "', Evaluation:'" + self.__relation.SourceNode.Evaluation + "', AgeInMilliseconds:'" + self.__relation.SourceNode.AgeInMilliseconds + "', AttentionLevel:'" + self.__relation.SourceNode.AttentionLevel + "', TV_keys: "+str(list(self.__relation.SourceNode.TruthValue.keys()))
        if self.__relation.SourceNode.TruthValue is not None:
            for key, value in zip(self.__relation.SourceNode.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query1 += ", " + str(key) + ":" + str(value)
        query1 += "})"

        query2 = " MERGE (m"
        for label in self.__relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + str(self.__relation.TargetNode.AoKID) + ", Value:" + str(self.__relation.TargetNode.Value) + ", SystemLevelType:'" + self.__relation.TargetNode.SystemLevelType + "', AbstractionLevel:'" + self.__relation.TargetNode.AbstractionLevel + "', Tag:'" + self.__relation.TargetNode.Tag + "', Validity:'" + self.__relation.TargetNode.Validity + "', ProcessingTag:'" + self.__relation.TargetNode.ProcessingTag + "', Evaluation:'" + self.__relation.TargetNode.Evaluation + "', AgeInMilliseconds:'" + self.__relation.TargetNode.AgeInMilliseconds + "', AttentionLevel:'" + self.__relation.TargetNode.AttentionLevel + "' , TV_keys: "+str(list(self.__relation.TargetNode.TruthValue.keys()))
        if self.__relation.TargetNode.TruthValue is not None:
            for key, value in zip(self.__relation.SourceNode.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query2 += ", " + str(key) + ":" + str(value)
        query2 += "})"
        return query1 + query2 + " Merge (n)-[r:" + self.__relation.RelationType + " {AoKID:'" + self.__relation.AoKID + "', RelationType:'" + self.__relation.RelationType + "', AttentionLevel: '" + self.__relation.AttentionLevel + "'}]-(m) return ID(n) as sid,ID(r) as rid,ID(m) as tid"

    def update_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " set r.AoKID= " + self.__relation.AoKID + ", r.RelationType= '" + self.__relation.RelationType + "', r.IsBiDirectional= '" + self.__relation.IsBiDirectional + "' ,r.AttentionLevel= '" + self.__relation.AttentionLevel + "' return 1"

    def retrieve_query(self, r_id):
        return "match (s)-[r]-(t) where ID(r)=" + r_id + " return s,r,t"

    def delete_relation_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " delete r return 1"

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
        return to_graph(response)

    def delete_relation(self, r_id):
        query = self.delete_relation_query(r_id)
        response = self.db.delete(query)

    def update_relation(self, r_id):
        query = self.update_query(r_id)
        response = self.db.update(query)


if __name__ == '__main__':
    node1=TNode(AoKID='1',Labels={"person1"},Value="4",SystemLevelType="abc",AbstractionLevel="first", Tag="abc", Validity="val",ProcessingTag="ptag",TruthValue={'Key1':'1234','Key2':'125'}, Evaluation="aaa",DateTimeStamp="10 April", AttentionLevel="1", AgeInMilliseconds="700")
    neo4=Neo4jNode(node1)
    SourseNode=neo4.retrieve_node("70")
    TargetNode=neo4.retrieve_node("71")
    rel1=TRelation(AoKID='4', Labels={"knows"},RelationType="KNOWS",SourceNode=SourseNode,TargetNode=TargetNode,Properties="abc",AttentionLevel="alevel",TruthValue={'RKey1':'1234','RKey2':'125'})
    neorel=Neo4jRelation(rel1)
    print(neorel.create_relation())