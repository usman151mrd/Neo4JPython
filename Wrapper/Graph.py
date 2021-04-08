class Graph:
    def __init__(self):
        self.ID = str
        self.Nodes = dict()  #map<string, TNode> Nodes;
        self.Edges = dict() #map<string, TRelation> Edges;
        self.RepresentationType = str #TERepresentationType RepresentationType