from Neo4JLayer.Neo4j import Neo4Niha
from Graph import Graph
from Relation import Relation
from Node import Node


class Neo4jGraph:
    def __init__(self, graph):
        self.graph = graph
        self.db = Neo4Niha()

    def retrieve_graph(self):
        query = "MATCH(m:HD)-[r:aka]->(n:HardDisk) return m,r,n LIMIT 25"
        response = self.db.retrieve(query)
        for node in response:
            # print(node)
            # print(node['m'].labels)
            # print(node['n'].labels)
           # print(node['r'].nodes[0])
            #print(node['r'].nodes[1])
            #print(node['r'].type)
            print(node['r'])
            properties = node.data()
            # print(properties['m'])
            # print(properties['r'])
            # print(properties['n'])

    def to_graph(self, response):
        tgraph1 = Graph

        for rel in response:
            data = rel.data()
            # print(data)
            # print(set(trelation1['n'].labels))
            # print(trelation1['n'].id)
            tgraph1.id = set(rel['n'].labels)
            tgraph1.Nodes = rel['n'].id
            tgraph1.Edges = data['n']['AoKID']
            # self.RepresentationType = str  # TERepresentationType RepresentationType

    def to_tnode(self, response):
        tnode1 = Node()

        for node in response:
            data = node.data()
            print(data)
            print(set(node['n'].labels))
            print(node['n'].id)
            tnode1.Labels = set(node['n'].labels)
            tnode1.Id = node['n'].id
            tnode1.AoKID = data['n']['AoKID']
            tnode1.AbstractionLevel = data['n']['AbstractionLevel']
            tnode1.AgeInMilliseconds = data['n']['AgeInMilliSeconds']
            tnode1.AttentionLevel = data['n']['AttentionLevel']
            tnode1.Value = data['n']['Value']
            tnode1.Validity = data['n']['Validity']
            tnode1.Tag = data['n']['Tag']
            tnode1.Evaluation = data['n']['Evaluation']
            tnode1.ProcessingTag = data['n']['ProcessingTag']
            tnode1.SystemLevelType = data['n']['SystemLevelType']
            tnode1.TruthValue = data['n']['TruthValue']
            print(node)

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


if __name__ == '__main__':
    g = Graph()
    n4j = Neo4jGraph(g)
    n4j.retrieve_graph()
