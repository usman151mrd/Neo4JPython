class Graph:
    def __init__(self):
        self.ID = str
        self.Nodes = dict()  # map<string, TNode> Nodes;
        self.Relation = dict()  # map<string, TRelation> Edges;
        self.RepresentationType = str  # TERepresentationType RepresentationType


'''
struct TGraph
{
    1: string ID;
    2: map<string, TNode> Nodes;
    3: map<string, TRelation> Relations;
    4: TERepresentationType RepresentationType;
}
create (n:Graph {type:"graph",id,rtype,rid=[]}) ->
struct TMemoryChunk
{
    1: required string ID;
    2: required string TimeStamp;
    3: TGraph Graph;
    4: required i16 Capacity;
    5: double AttentionLevel;
    6: double DecayLevel;//-1
    7: double Importance;
    8: double Evaluation;
}
'''
