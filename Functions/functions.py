import json
from niha_thrift.ttypes import TGraph, TNode, TRelation, TMemoryChunk


def load_config():
    with open(r"C:\Users\User\Downloads\neo4python\neo4python\Functions\config.json") as json_data_file:
        data = json.load(json_data_file)
    conf = data["neo4j"]
    scheme = conf["scheme"]
    host = conf["host"]
    port = conf["port"]
    user = conf["user"]
    password = conf["password"]
    url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host, port=port)
    return url, user, password


def to_relation(_id, source, target, _relation, rel_properties):
    relation = TRelation()
    relation.Labels = _relation
    relation.Neo4jId = str(_id)
    relation.AoKID = str(rel_properties['AoKID'])
    relation.RelationType = str(rel_properties['RelationType'])
    relation.SourceNode = source
    relation.TargetNode = target
    relation.IsBiDirectional = False
    #relation.Properties = rel_properties
    relation.AttentionLevel = rel_properties['AttentionLevel']
    tv_dict = dict()
    for key in rel_properties['Keys']:
        tv_dict[key] = rel_properties[key]
    relation.TruthValue = tv_dict
    return relation


def to_graph(response):
    graph = TGraph()
    _nodes = dict()
    _edges = dict()
    for node in response:
        source_node = to_tnode(node['r'].nodes[0])
        target_node = to_tnode(node['r'].nodes[1])
        _id = node['r'].id
        _type = node['r'].type
        properties = dict(node['r'])
        relation = to_relation(_id, source_node, target_node, _type, properties)
        _nodes[source_node.Neo4jID] = source_node
        _nodes[target_node.Neo4jID] = target_node
        _edges[_id] = relation
    graph.Nodes = _nodes
    graph.Relation = _edges

    return graph


def to_tnode(_node):
    node = TNode()
    properties = dict(_node)
    node.Labels = set(_node.labels)
    node.Neo4jID = str(_node.id)
    node.AoKID = str(properties['AoKID'])
    node.AbstractionLevel = properties['AbstractionLevel']
    node.AgeInMilliseconds = properties['AgeInMilliseconds']
    node.AttentionLevel = properties['AttentionLevel']
    node.Value = str(properties['Value'])
    node.Validity = properties['Validity']
    node.Tag = properties['Tag']
    node.Evaluation = properties['Evaluation']
    node.ProcessingTag = properties['ProcessingTag']
    node.SystemLevelType = properties['SystemLevelType']
    tv_dict = dict()
    for key in properties['Keys']:
        tv_dict[key] = properties[key]
    node.TruthValue = tv_dict
    return node


def merge_node(t_node):
    query = "Merge (n"
    for label in t_node.node.Labels:
        query += ":{label}".format(label=label)
    query += " {AoKID:" + t_node.node.AoKID + ", Value:" + t_node.node.Value + ", SystemLevelType:" + t_node.node.SystemLevelType + ", AbstractionLevel:" + t_node.node.AbstractionLevel + ", Tag:" + t_node.node.Tag + ", Validity:" + t_node.node.Validity + ", ProcessingTag:" + t_node.node.ProcessingTag + ", Evaluation:" + t_node.node.Evaluation + ", DateTimeStamp:" + t_node.node.DateTimeStamp + ", AgeInMilliseconds:" + t_node.node.AgeInMilliseconds + ", AttentionLevel:" + t_node.node.AttentionLevel
    for key, value in zip(t_node.node.TruthValue.keys(), t_node.node.TruthValue.values()):
        # print(key, value)
        query += ", TV_" + key + ":" + value
    query += "})"
    return query
