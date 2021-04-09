from Neo4JLayer.Neo4j import Neo4Niha
from Node import Node


class Neo4jNode:
    def __init__(self, node):
        self.node = node
        self.db = Neo4Niha()

    def create_query(self):
        query = "CREATE (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += " {AoKID:" + self.node.AoKID + ", Value:" + self.node.Value + ", SystemLevelType:" + self.node.SystemLevelType + ", AbstractionLevel:" + self.node.AbstractionLevel + ", Tag:" + self.node.Tag + ", Validity:" + self.node.Validity + ", ProcessingTag:" + self.node.ProcessingTag + ", Evaluation:" + self.node.Evaluation + ", DateTimeStamp:" + self.node.DateTimeStamp + ", AgeInMilliseconds:" + self.node.AgeInMilliseconds + ", AttentionLevel:" + self.node.AttentionLevel
        for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
            # print(key, value)
            query += ", TV_" + key + ":" + value
        query += "}) RETURN n"
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

    def update_query(self):
        query = "MATCH (n"
        for label in self.node.Labels:
            query += ":{label}".format(label=label)
        query += " {name: '" + self.node.name + "'}) SET "
        query += " n.AoKID=" + self.node.AoKID + ", n.Value=" + self.node.Value + ", n.SystemLevelType=" + self.node.SystemLevelType + ", n.AbstractionLevel=" + self.node.AbstractionLevel + ", n.Tag=" + self.node.Tag + ", n.Validity=" + self.node.Validity + ", n.ProcessingTag=" + self.node.ProcessingTag + ", n.Evaluation=" + self.node.Evaluation + ", n.DateTimeStamp=" + self.node.DateTimeStamp + ", n.AgeInMilliseconds=" + self.node.AgeInMilliseconds + ", n.AttentionLevel=" + self.node.AttentionLevel
        for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
            # print(key, value)
            query += ", n.TV_" + key + "=" + value
        query += "return n"
        print(query)

    def create_node(self):
        # query = self.create_query()
        query = "CREATE(m:trial {name:'trial', domain:'trial'}) return m"
        response = self.db.create(query)

    def retrieve_node(self):
        # query = self.retrieve_query()
        query = "MATCH(n:Test) RETURN n"
        response = self.db.retrieve(query)
        self.to_tnode(response)

    def delete_node(self):
        #query = self.delete_query()
        query = "MATCH (n:Laptop) DETACH DELETE n"
        response = self.db.delete(query)

    def update_node(self):
        query = "MATCH (n:TEST1 {name:'TEST1'}) SET n.AoKID=10 return n"
        print(query)
        response = self.db.update(query)

    def to_tnode(self, response):
        node = Node()

        for _node in response:
            data = _node.data()
            print(data)
            print(set(_node['n'].labels))
            print(_node['n'].id)
            node.Labels = set(_node['n'].labels)
            node.Id = _node['n'].id
            node.AoKID = data['n']['AoKID']
            node.AbstractionLevel = data['n']['AbstractionLevel']
            node.AgeInMilliseconds = data['n']['AgeInMilliSeconds']
            node.AttentionLevel = data['n']['AttentionLevel']
            node.Value = data['n']['Value']
            node.Validity = data['n']['Validity']
            node.Tag = data['n']['Tag']
            node.Evaluation = data['n']['Evaluation']
            node.ProcessingTag = data['n']['ProcessingTag']
            node.SystemLevelType = data['n']['SystemLevelType']
            # tnode1.TruthValue = data['n']['TruthValue']
            print(_node)


if __name__ == '__main__':
    node = Node
    tnode = Neo4jNode(node)
    # tnode.retrieve_node()
    tnode.update_node()
