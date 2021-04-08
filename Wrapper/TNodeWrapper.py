from Neo4JLayer.Neo4j import Neo4Niha
from Node import TNode


class Neo4jNode:
    def __init__(self, node):
        self.node = node
        self.db = Neo4Niha()

    def create_query(self):
        query = "create (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += " {AoKID:" + self.node.AoKID + ", Value:" + self.node.Value + ", SystemLevelType:" + self.node.SystemLevelType + ", AbstractionLevel:" + self.node.AbstractionLevel + ", Tag:" + self.node.Tag + ", Validity:" + self.node.Validity + ", ProcessingTag:" + self.node.ProcessingTag + ", Evaluation:" + self.node.Evaluation + ", DateTimeStamp:" + self.node.DateTimeStamp + ", AgeInMilliseconds:" + self.node.AgeInMilliseconds + ", AttentionLevel:" + self.node.AttentionLevel
        for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
            # print(key, value)
            query += ", TV_" + key + ":" + value
        query += "})"
        return query

    def delete_query(self):
        query = "MATCH (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += "WHERE n.Neo4jID=" + self.node.Neo4jID + " DELETE n"
        return query

    def retrieve_query(self):
        query = "MATCH (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += "WHERE n.Neo4jID=" + self.node.Neo4jID + " RETURN n"
        return query

    def create_node(self):
        query = self.create_query()
        response = self.db.create(query)

    def retrieve_node(self):
        # query = self.retrieve_query()
        query = "MATCH(n:Test) RETURN n"
        response = self.db.retrieve(query)
        self.to_tnode(response)

    def delete_node(self):
        query = self.delete_query()
        response = self.db.delete(query)

    def to_tnode(self, response):
        tnode1 = TNode()

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


if __name__ == '__main__':
    node = TNode
    tnode = Neo4jNode(node)
    tnode.retrieve_node()
