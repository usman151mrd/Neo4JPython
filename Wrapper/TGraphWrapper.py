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
        self.to_graph(response)

    def to_graph(self, response):
        _nodes = dict()
        _edges = dict()
        for node in response:
            source_node = self.to_tnode(node['r'].nodes[0])
            target_node = self.to_tnode(node['r'].nodes[1])
            _id = node['r'].id
            _type = node['r'].type
            properties = dict(node['r'])
            relation = self.to_relation(_id, source_node, target_node, _type, properties)
            if source_node.Labels[0] not in _nodes.keys():
                _nodes[source_node.Labels[0]] = source_node
            if target_node.Labels[0] not in _nodes.keys():
                _nodes[target_node.Labels[0]] = source_node
            key = "{source}-{relation}-{target}".format(source=source_node.Labels[0],relation=_type, target=target_node.Labels[0])
            _edges[key] = relation
        self.graph.Nodes = _nodes
        self.graph.Edges = _edges

    def to_tnode(self, _node):
        node = Node()
        print("38 : ", _node)
        print(set(_node.labels))
        print(_node.id)
        properties = dict(_node)
        node.Labels = set(_node.labels)
        node.Id = _node.id
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

    def to_relation(self, _id, source, target, _relation, rel_properties):
        relation = Relation()
        relation.Labels = _relation
        relation.Neo4jId = _id
        relation.AoKID = rel_properties['AoKID']
        relation.RelationType = rel_properties['RelationType']
        relation.SourceNode = source
        relation.TargetNode = target
        relation.IsBiDirectional = False
        relation.Properties = rel_properties
        relation.AttentionLevel = 0.0
        relation.TruthValue = dict()
        return relation


if __name__ == '__main__':
    g = Graph()
    n4j = Neo4jGraph(g)
    n4j.retrieve_graph()
    print("nodes : ", g.Nodes)
    print("edges : ", g.Edges)
