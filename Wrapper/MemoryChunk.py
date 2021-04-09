from Graph import Graph


class MemoryChunk:
    def __init__(self):
        self.ID = str()
        self.TimeStamp = str()
        self.Graph = Graph
        self.Capacity = int()
        self.AttentionLevel = 0.0
        self.DecayLevel = int()
        self.Importance = 0.0
        self.Evaluation = 0.0
        self.Nid=list()
        self.Rid=list()
        self.rtype=str()
        self.label=list()
