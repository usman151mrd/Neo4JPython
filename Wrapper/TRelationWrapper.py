from Neo4JLayer.Neo4j import Neo4Niha
from Node import TNode
from Relation import Relation


class Neo4jRelation:
    def __init__(self, relation):
        self.relation = relation
        self.db = Neo4Niha()

    def create_query(self):
        query1 = "MATCH (n"
        for label in self.relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.relation.SourceNode.AoKID + ", Value:" + self.relation.SourceNode.Value + ", SystemLevelType:" + self.relation.SourceNode.SystemLevelType + ", AbstractionLevel:" + self.relation.SourceNode.AbstractionLevel + ", Tag:" + self.relation.SourceNode.Tag + ", Validity:" + self.relation.SourceNode.Validity + ", ProcessingTag:" + self.relation.SourceNode.ProcessingTag + ", Evaluation:" + self.relation.SourceNode.Evaluation + ", DateTimeStamp:" + self.relation.SourceNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.SourceNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.SourceNode.AttentionLevel
        for key, value in zip(self.relation.SourceNode.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
            # print(key, value)
            query1 += ", TV_" + key + ":" + value
        query1 += "})"

        query2 = "MATCH (m"
        for label in self.relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + self.relation.TargetNode.AoKID + ", Value:" + self.relation.TargetNode.Value + ", SystemLevelType:" + self.relation.TargetNode.SystemLevelType + ", AbstractionLevel:" + self.relation.TargetNode.AbstractionLevel + ", Tag:" + self.relation.TargetNode.Tag + ", Validity:" + self.relation.TargetNode.Validity + ", ProcessingTag:" + self.relation.TargetNode.ProcessingTag + ", Evaluation:" + self.relation.TargetNode.Evaluation + ", DateTimeStamp:" + self.relation.TargetNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.TargetNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.TargetNode.AttentionLevel
        for key, value in zip(self.relation.TruthValue.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
            # print(key, value)
            query2 += ", TV_" + key + ":" + value
        query2 += "})"
        if self.relation.IsBiDirectional:
            query = query1 + query2 + "CREATE p=(:n)-[r:" + self.relation.RelationType + "]-(:m) return p"
        else:
            query = query1 + query2 + "CREATE p=(:n)->[r:" + self.relation.RelationType + "]->(:m) return p"
        return query

    def delete_query(self):
        query = "MATCH (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += "WHERE n.Neo4jID=" + self.node.Neo4jID + " DELETE n"
        return query

    def retrieve_query(self):
        query1 = "MATCH (n"
        for label in self.relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.relation.SourceNode.AoKID + ", Value:" + self.relation.SourceNode.Value + ", SystemLevelType:" + self.relation.SourceNode.SystemLevelType + ", AbstractionLevel:" + self.relation.SourceNode.AbstractionLevel + ", Tag:" + self.relation.SourceNode.Tag + ", Validity:" + self.relation.SourceNode.Validity + ", ProcessingTag:" + self.relation.SourceNode.ProcessingTag + ", Evaluation:" + self.relation.SourceNode.Evaluation + ", DateTimeStamp:" + self.relation.SourceNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.SourceNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.SourceNode.AttentionLevel
        for key, value in zip(self.relation.SourceNode.TruthValue.keys(), self.relation.DestinationNode.TruthValue.values()):
            # print(key, value)
            query1 += ", TV_" + key + ":" + value
        query1 += "})"

        query2 = "MATCH (m"
        for label in self.relation.TargetNode.Labels:
            query2 += ":{label}".format(label=label)
        query2 += " {AoKID:" + self.relation.TargetNode.AoKID + ", Value:" + self.relation.TargetNode.Value + ", SystemLevelType:" + self.relation.TargetNode.SystemLevelType + ", AbstractionLevel:" + self.relation.TargetNode.AbstractionLevel + ", Tag:" + self.relation.TargetNode.Tag + ", Validity:" + self.relation.TargetNode.Validity + ", ProcessingTag:" + self.relation.TargetNode.ProcessingTag + ", Evaluation:" + self.relation.TargetNode.Evaluation + ", DateTimeStamp:" + self.relation.TargetNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.TargetNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.TargetNode.AttentionLevel
        for key, value in zip(self.relation.TruthValue.TruthValue.keys(), self.relation.TargetNode.TruthValue.values()):
            # print(key, value)
            query2 += ", TV_" + key + ":" + value
        query2 += "})"
        if self.relation.IsBiDirectional:
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + "]-(:m) return p"
        else:
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + "]->(:m) return p"
        return query

    def create_relation(self):
        query = self.create_query()
        response = self.db.create(query)

    def retrieve_relation(self):
        # query = self.retrieve_query()
        query = "MATCH(n:Test) RETURN n"
        response = self.db.retrieve(query)
        self.to_trelation(response)

    def delete_relation(self):
        query = self.delete_query()
        response = self.db.delete(query)

    def to_trelation(self, response):
        trelation1 = Relation

        for rel in response:
            data = rel.data()
            print(data)
            print(set(trelation1['n'].labels))
            print(trelation1['n'].id)
            trelation1.Labels = set(rel['n'].labels)
            trelation1.Neo4jId = rel['n'].id
            trelation1.AoKID = data['n']['AoKID']
            trelation1.RelationType = data['n']['RelationType']
            trelation1.SourceNode = data['n']['SourceNode']
            trelation1.TargetNode = data['n']['TargetNode']
            trelation1.IsBiDirectional = data['n']['IsBiDirectional']
            trelation1.Properties = data['n']['Properties']
            trelation1.AttentionLevel = data['n']['AttentionLevel']
            trelation1.TruthValue = data['n']['TruthValue']
            print(rel)