from Node import Node


class Relation:
    def __init__(self):
        self.Neo4jID = str()
        self.AoKID = str()
        self.Labels = set()  # set<string> Labels
        self.RelationType = str()
        self.SourceNode = Node  # TNode SourceNode
        self.TargetNode = Node  # TNode TargetNode
        self.Properties = dict()  # map<string, TDimension> Properties
        self.AttentionLevel = 0.0
        self.TruthValue = dict()  # map<string, double> TruthValue
