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

       # for node in response:
        #   print(node)
        #   print(node['m'].labels)
        #   print(node['n'].labels)
            #print(node['r'].nodes[0])
            #print(node['r'].nodes[1])
        #     #print(node['r'].type)
        #     print(node['r'])
        #     properties = node.data()
        #     #print(properties['m'])
        #     #print(properties['r'])
        #     #print(properties['n'])
        self.to_graph(response)

    def to_graph(self, response):
        g = Graph
        _nodes = dict()
        _edges = dict()
        for node in response:
            source_node = self.to_tnode((node['r'].nodes[0]))
            target_node = self.to_tnode((node['r'].nodes[1]))
            _id = node['r'].id
            _type = node['r'].type
            properties = dict(node['r'])
            relation = self.to_relation(_id, source_node, target_node, _type, properties)
            if source_node.Labels[0] not in _nodes.keys():
                _nodes[source_node.Labels[0]] = source_node

    def to_tnode(self, node):
        node = Node()
        properties = node.data()
        print(set(node.labels))
        print(node.id)
        node.Labels = set(node['n'].labels)
        node.Id = node['n'].id
        node.AoKID = properties['AoKID']
        node.AbstractionLevel = properties['AbstractionLevel']
        node.AgeInMilliseconds = properties['AgeInMilliSeconds']
        node.AttentionLevel = properties['AttentionLevel']
        node.Value = properties['Value']
        node.Validity = properties['Validity']
        node.Tag = properties['Tag']
        node.Evaluation = properties['Evaluation']
        node.ProcessingTag = properties['ProcessingTag']
        node.SystemLevelType = properties['SystemLevelType']
        # node.TruthValue = properties['TruthValue']
        return node

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
