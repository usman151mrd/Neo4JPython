from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import *


def retrieve_query(r_id):
    return "match (s)-[r]-(t) where ID(r)=" + r_id + " return s,r,t"


def delete_relation_query(_id):
    return "match ()-[r]-() where ID(r)=" + _id + " delete r"


class Neo4jRelation:
    def __init__(self, relation):
        self.relation = relation
        self.db = Neo4Niha()

    def create_query(self):
        query1 = "MERGE (n"
        for label in self.relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.relation.SourceNode.AoKID + ", Value:" + self.relation.SourceNode.Value + ", SystemLevelType:" + self.relation.SourceNode.SystemLevelType + ", AbstractionLevel:" + self.relation.SourceNode.AbstractionLevel + ", Tag:" + self.relation.SourceNode.Tag + ", Validity:" + self.relation.SourceNode.Validity + ", ProcessingTag:" + self.relation.SourceNode.ProcessingTag + ", Evaluation:" + self.relation.SourceNode.Evaluation + ", DateTimeStamp:" + self.relation.SourceNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.SourceNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.SourceNode.AttentionLevel
        for key, value in zip(self.relation.SourceNode.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
            # print(key, value)
            query1 += ", TV_" + key + ":" + value
        query1 += "})"

        query2 = "MERGE (m"
        for label in self.relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + self.relation.TargetNode.AoKID + ", Value:" + self.relation.TargetNode.Value + ", SystemLevelType:" + self.relation.TargetNode.SystemLevelType + ", AbstractionLevel:" + self.relation.TargetNode.AbstractionLevel + ", Tag:" + self.relation.TargetNode.Tag + ", Validity:" + self.relation.TargetNode.Validity + ", ProcessingTag:" + self.relation.TargetNode.ProcessingTag + ", Evaluation:" + self.relation.TargetNode.Evaluation + ", DateTimeStamp:" + self.relation.TargetNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.TargetNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.TargetNode.AttentionLevel
        for key, value in zip(self.relation.TruthValue.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
            # print(key, value)
            query2 += ", TV_" + key + ":" + value
        query2 += "})"
        return query1 + query2 + "Merge p=(n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]-(m) return ID(n),ID(r),ID(m)"

    def update_query(self):
        pass  # update by sabahat

    def create_relation(self):
        query = self.create_query()
        response = self.db.create(query)
        return response

    def retrieve_relation(self):
        query = retrieve_query()
        response = self.db.retrieve(query)
        self.to_trelation(response)

    def delete_relation(self):
        query = delete_relation_query(0)
        response = self.db.delete(query)

    def update_relation(self):
        query = self.update_query()
        print(query)
        response = self.db.update(query)


if __name__ == '__main__':
    relation = TRelation
    trelation = Neo4jRelation(relation)
    trelation.create_relation()
    # trelation.retrieve_relation()
    # trelation.update_relation()
    # trelation.delete_relation()
