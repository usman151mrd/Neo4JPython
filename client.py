#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import sys
import glob

sys.path.append(r'C:\Users\User\Downloads\neo4python\neo4python\genpy')

from genpy.niha_thrift import Neo4jGraph
from genpy.niha_thrift import Neo4jRelation
from genpy.niha_thrift import Neo4jNode
from genpy.niha_thrift import Neo4jMemoryChunk
from genpy.niha_thrift.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('127.0.0.1', 9091)
    transport1 = TSocket.TSocket('127.0.0.1', 9090)
    transport2 = TSocket.TSocket('127.0.0.1', 9092)
    transport3 = TSocket.TSocket('127.0.0.1', 9093)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
    transport1 = TTransport.TBufferedTransport(transport1)
    transport2= TTransport.TBufferedTransport(transport2)
    transport3= TTransport.TBufferedTransport(transport3)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    protocol1 = TBinaryProtocol.TBinaryProtocol(transport1)
    protocol2 = TBinaryProtocol.TBinaryProtocol(transport2)
    protocol3 = TBinaryProtocol.TBinaryProtocol(transport3)

    # Create a client to use the protocol encoder
    client = Neo4jNode.Client(protocol)
    client1 = Neo4jRelation.Client(protocol1)
    client2 = Neo4jGraph.Client(protocol2)
    client3 = Neo4jMemoryChunk.Client(protocol3)

    # Connect!
    #transport.open()
    #transport1.open()
    transport2.open()
    #transport3.open()
    TS=TESystemLevelType.STRING
    TA=TEAbstractionLevel.INSTANCE_NODE
    SNode = TNode(AoKID="5", Labels={"person11"}, Value="4", SystemLevelType=TS, AbstractionLevel=TA, Tag="abc",
                 Validity="val", ProcessingTag="ptag", TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
                 DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0, Domains={"Human", "Living"})
    TS = TESystemLevelType.STRING
    TA = TEAbstractionLevel.INSTANCE_NODE
    TNOde = TNode(AoKID="5", Labels={"person111"}, Value="4", SystemLevelType=TS, AbstractionLevel=TA, Tag="abc",
                  Validity="val", ProcessingTag="ptag", TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
                  DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0, Domains={"Human", "Living"})
    #SNode = client.retrieve("140")
    #TNOde = client.retrieve("100")
    #print(SNode)
    #print(TNOde)
    rel = TRelation(AoKID="101", Labels={"Fiend_of"},SourceNode=SNode, TargetNode=TNOde, RelationType="trial",
                    TruthValue={'Key1': 1234.0, 'Key2': 125.0}, AttentionLevel=1.0)
    #print(rel)
    #response=client1.update(rel,"105")
    RT=TERepresentationType.CONCEPTUAL_GRAPH
    graph=TGraph(Nodes={"sourcenode":SNode, "TargetNode":TNode}, Relations={"relation":rel}, RepresentationType=RT)
    response=client2.create(graph=graph)
    print("response : ", response)
    # node2 = TNode(AoKID="1", Labels={"person11"}, Value="4", SystemLevelType="abc", AbstractionLevel="first", Tag="abc",
    #               Validity="val", ProcessingTag="ptag", TruthValue={'Key1': '1234', 'Key2': '125'}, Evaluation="aaa",
    #               DateTimeStamp="10 April", AttentionLevel=1, AgeInMilliseconds=0.0)
    # response = client.create(node2)
    # print("response : ", response)
    # node3 = TNode(AoKID="1", Labels={"person12"}, Value="4", SystemLevelType="abc", AbstractionLevel="first", Tag="abc",
    #               Validity="val", ProcessingTag="ptag", TruthValue={'Key1': '1234', 'Key2': '125'}, Evaluation="aaa",
    #               DateTimeStamp="10 April", AttentionLevel=1, AgeInMilliseconds=0.0)
    # response = client.create(node3)
    # print("response : ", response)


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
