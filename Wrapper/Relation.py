from Node import TNode


class Relation:
    def __init__(self):
        self.Neo4jID = str
        self.AoKID = str
        self.Labels = set  # set<string> Labels
        self.RelationType = str
        self.SourceNode = TNode  # TNode SourceNode
        self.TargetNode = TNode  # TNode TargetNode
        self.IsBiDirectional = bool
        self.Properties = map  # map<string, TDimension> Properties
        self.AttentionLevel = 0.0
        self.TruthValue = map  # map<string, double> TruthValue
