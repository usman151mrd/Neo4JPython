from Neo4JLayer.Neo4j import Neo4Niha
from Node import Node
from Relation import Relation


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
        if self.relation.IsBiDirectional:
            query = query1 + query2 + "CREATE p=(:n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]-(:m) return n,r,m"
        else:
            query = query1 + query2 + "CREATE p=(:n)->[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]->(:m) return n,r,m"
        return query

    def delete_query(self):
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
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]-(:m) delete r"
        else:
            query = query1 + query2 + "MATCH p=(:n)->[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]->(:m) delete r"
        return query

    def retrieve_query(self):
        query1 = "MATCH (n"
        for label in self.relation.SourceNode.Labels:
            query1 += ":{label}".format(label=label)
        query1 += " {AoKID:" + self.relation.SourceNode.AoKID + ", Value:" + self.relation.SourceNode.Value + ", SystemLevelType:" + self.relation.SourceNode.SystemLevelType + ", AbstractionLevel:" + self.relation.SourceNode.AbstractionLevel + ", Tag:" + self.relation.SourceNode.Tag + ", Validity:" + self.relation.SourceNode.Validity + ", ProcessingTag:" + self.relation.SourceNode.ProcessingTag + ", Evaluation:" + self.relation.SourceNode.Evaluation + ", DateTimeStamp:" + self.relation.SourceNode.DateTimeStamp + ", AgeInMilliseconds:" + self.relation.SourceNode.AgeInMilliseconds + ", AttentionLevel:" + self.relation.SourceNode.AttentionLevel
        for key, value in zip(self.relation.SourceNode.TruthValue.keys(),
                              self.relation.DestinationNode.TruthValue.values()):
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
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]-(:m) return n,r,m"
        else:
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + " {AoKID:'" + self.relation.AoKID + "', AttentionLevel: '" + self.relation.AttentionLevel + "'}]->(:m) return n,r,m"
        return query

    def update_query(self):
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
            query = query1 + query2 + "MATCH p=(:n)-[r:" + self.relation.RelationType + "]-(:m) SET  r.AoKID='" + self.relation.AoKID + "', r.AttentionLevel= '" + self.relation.AttentionLevel + "' return n,r,m"
        else:
            query = query1 + query2 + "MATCH p=(:n)->[r:" + self.relation.RelationType + "]->(:m) SET  r.AoKID='" + self.relation.AoKID + "', r.AttentionLevel= '" + self.relation.AttentionLevel + "' return n,r,m"
        return query

    def create_relation(self):
        # query = self.create_query()
        query1 = "MERGE(m: TEST3 {name: 'TEST3', AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'}) "
        query2 = "MERGE(n: TEST4 {name: 'TEST4' ,AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'})"
        query = query1 + query2 + " CREATE p=(m)-[r:isA {AoKID:'2', RelationType:'testing', AttentionLevel:'0.0'}]->(n) return r"
        response = self.db.create(query)
        return response

    def retrieve_relation(self):
        # query = self.retrieve_query()
        query1 = "MATCH(m: TEST3 {name: 'TEST3', AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'}) "
        query2 = "MATCH(n: TEST4 {name: 'TEST4', AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'})"
        query = query1 + query2 + " MATCH p=(m)-[r:isA {AoKID:'2', RelationType:'testing', AttentionLevel:'0.0'}]->(n) return r"
        print(query)
        response = self.db.retrieve(query)
        self.to_trelation(response)

    def delete_relation(self):
        # query = self.delete_query()
        query1 = "MATCH(m: TEST3 {name: 'TEST3', AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'}) "
        query2 = "MATCH(n: TEST4 {name: 'TEST4' ,AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'})"
        query = query1 + query2 + " MATCH p=(m)-[r:isA {AoKID:'2', RelationType:'testig', AttentionLevel:'0.1'}]->(n) delete r"
        response = self.db.delete(query)

    def update_relation(self):
        # query = self.update_query()
        query1 = "MATCH(m: TEST3 {name: 'TEST3' ,AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'}) "
        query2 = "MATCH(n: TEST4 {name: 'TEST4' ,AbstractionLevel: '22', AgeInMilliSeconds: '702', AoKID: '42', AttentionLevel: '72',DateTimeStamp: '8April', Evaluation: 'qwe2', ProcessingTag: 'www2', SystemLevelType: 'INT16', Tag: 'ss2',Validity: 'Not>20', Value: '6'}) "
        query = query1 + query2 + "MATCH p=(m)-[r:isA]->(n) SET r.AoKID='2', r.RelationType='testig', r.AttentionLevel='0.1' return r"
        print(query)
        response = self.db.update(query)

    def to_trelation(self, response):
        trelation1 = Relation

        for rel in response:
            #print(rel)
            data = rel.data()
            # print(data)
            # print(rel['r'].type)
            # print(rel['r'].id)
            properties = dict(rel['r'])
            trelation1.Labels = set(rel['r'].type)
            trelation1.Neo4jId = rel['r'].id
            trelation1.AoKID = properties['AoKID']
            trelation1.RelationType = properties['RelationType']
            # trelation1.SourceNode = data['n']['SourceNode']
            # trelation1.TargetNode = data['n']['TargetNode']
            trelation1.IsBiDirectional = False
            trelation1.Properties = properties
            trelation1.AttentionLevel = 0.0
            # trelation1.TruthValue = dict()
            print(trelation1)

if __name__ == '__main__':
    relation = Relation
    trelation = Neo4jRelation(relation)
    trelation.create_relation()
    #trelation.retrieve_relation()
    #trelation.update_relation()
    #trelation.delete_relation()
