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

# sys.path.append(r'genpy')

from genpy.niha_thrift import Neo4Niha
from genpy.niha_thrift.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('127.0.0.1', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Neo4Niha.Client(protocol)

    # Connect!
    transport.open()

    TS = TESystemLevelType.STRING
    TA = TEAbstractionLevel.INSTANCE_NODE
    SNode = TNode(AoKID="5", Labels={"person11"}, Value="4", SystemLevelType=TS, AbstractionLevel=TA, Tag="abc",
                  Validity="val", ProcessingTag="ptag", TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
                  DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0, Domains={"Human", "Living"})
    #response1 = client.createNode(Node)
    #print("response : ", response1)

    TNOde = TNode(AoKID="5", Labels={"person111"}, Value="4", SystemLevelType=TS, AbstractionLevel=TA, Tag="abc",
                  Validity="val", ProcessingTag="ptag", TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
                  DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0, Domains={"Human", "Living"})
    #response2 = client.createNode(Node1)
    #print("response : ", response2)
    #SNode = client.retrieveNode("166")
    #TNOde = client.retrieveNode("167")
    #print(SNode)
    #print(TNOde)
    rel = TRelation(AoKID="101", Labels={"Fiend_of"}, SourceNode=SNode, TargetNode=TNOde, RelationType="trial",
                    TruthValue={'Key1': 1234.0, 'Key2': 125.0}, AttentionLevel=1.0)
    # print(rel)
    response=client.createRelation(rel)
    print("response : ", response)
    # RT = TERepresentationType.SEMANTIC_NETWORK
    # graph = TGraph(Neo4jID='148', Nodes={"140": SNode, "141": TNOde}, Relations={"relation": rel},
    #                RepresentationType=RT)
    # #print(graph)
    # memoryChunk = TMemoryChunk(TimeStamp='timestamp', Graph=graph, Capacity=10, AttentionLevel=100.0, DecayLevel=1.0,
    #                            Evaluation=0.0, Importance=9.0)
    # response = client3.retrieve("155")
    # print(type(response))
    # print("response : ", response)
    # # node2 = TNode(AoKID="1", Labels={"person11"}, Value="4", SystemLevelType="abc", AbstractionLevel="first", Tag="abc",
    # #               Validity="val", ProcessingTag="ptag", TruthValue={'Key1': '1234', 'Key2': '125'}, Evaluation="aaa",
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
