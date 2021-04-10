import datetime

from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import *
from Functions.functions import *
from TNodeWrapper import Neo4jNode


class Neo4jRelation:
    def __init__(self, relation):
        self.relation = relation
        self.db = Neo4Niha()

    def create_query(self):
        print(self.relation.SourceNode)
        print(self.relation.TargetNode)
        query1 = "MERGE (n"
        for label in self.relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.relation.SourceNode.AoKID + ", Value:" + self.relation.SourceNode.Value + ", SystemLevelType:'" + self.relation.SourceNode.SystemLevelType + "', AbstractionLevel:'" + self.relation.SourceNode.AbstractionLevel + "', Tag:'" + self.relation.SourceNode.Tag + "', Validity:'" + self.relation.SourceNode.Validity + "', ProcessingTag:'" + self.relation.SourceNode.ProcessingTag + "', Evaluation:'" + self.relation.SourceNode.Evaluation + "', AgeInMilliseconds:'" + self.relation.SourceNode.AgeInMilliseconds + "', AttentionLevel:'" + self.relation.SourceNode.AttentionLevel+"'"
        if self.relation.SourceNode.TruthValue is not None:
            for key, value in zip(self.relation.SourceNode.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query1 += ", TV_" + key + ":" + value
        query1 += "})"

        query2 = " MERGE (m"
        for label in self.relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + self.relation.TargetNode.AoKID + ", Value:" + self.relation.TargetNode.Value + ", SystemLevelType:'" + self.relation.TargetNode.SystemLevelType + "', AbstractionLevel:'" + self.relation.TargetNode.AbstractionLevel + "', Tag:'" + self.relation.TargetNode.Tag + "', Validity:'" + self.relation.TargetNode.Validity + "', ProcessingTag:'" + self.relation.TargetNode.ProcessingTag + "', Evaluation:'" + self.relation.TargetNode.Evaluation + "', AgeInMilliseconds:'" + self.relation.TargetNode.AgeInMilliseconds + "', AttentionLevel:'" + self.relation.TargetNode.AttentionLevel+"'"
        if self.relation.TargetNode.TruthValue is not None:
            for key, value in zip(self.relation.TruthValue.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
                # print(key, value)
                query2 += ", TV_" + key + ":" + value
        query2 += "})"
        return query1 + query2 + " Merge p=(n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', RelationType:'"+ self.relation.RelationType+"', AttentionLevel: '" + self.relation.AttentionLevel + "'}]-(m) return n,r,m"

    def update_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " set r.AoKID= " + self.relation.AoKID + ", r.RelationType= '" + self.relation.RelationType + "', r.IsBiDirectional= '" + self.relation.IsBiDirectional + "' ,r.AttentionLevel= '" + self.relation.AttentionLevel +  "' return r"

    def retrieve_query(self, r_id):
        return "match (s)-[r]-(t) where ID(r)=" + r_id + " return s,r,t"

    def delete_relation_query(self, r_id):
        return "match ()-[r]-() where ID(r)=" + r_id + " delete r"

    def create_relation(self):
        query = self.create_query()
        print(query)
        response = self.db.create(query)
        return to_graph(response)

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


if __name__ == '__main__':
    node = TNode(AoKID="1", Labels={"Tester"}, Value="1", SystemLevelType="abc", AbstractionLevel="1", Tag="Abs",
                 Validity="not > 20", ProcessingTag="ptag", Evaluation="123",
                 DateTimeStamp=str(datetime.datetime.now()), AgeInMilliseconds="600", AttentionLevel="1")
    tnode = Neo4jNode(node)
    #nod = tnode.create_node()
    SourceNode = tnode.retrieve_node("32")
    #print("source",SourceNode)
    TargetNode = tnode.retrieve_node("1")
    #print("target",TargetNode)
    relation = TRelation(AoKID="25", Labels={"trial"}, RelationType="trial", SourceNode=SourceNode, TargetNode=TargetNode,
                         IsBiDirectional="True", AttentionLevel="3")
    trelation = Neo4jRelation(relation)
    trelation.create_relation()
    #trelation.retrieve_relation("53")
    #trelation.update_relation("53")
    #trelation.delete_relation("53")
    # def __init__(self, Neo4jID=None, AoKID=None, Labels=None, RelationType=None, SourceNode=None, TargetNode=None, IsBiDirectional=None, Properties=None, AttentionLevel=None, TruthValue=None,):
