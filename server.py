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

import glob
import sys

# sys.path.append(r'C:\Users\User\Downloads\neo4python\neo4python')

from genpy.niha_thrift import Neo4jGraph
from genpy.niha_thrift import Neo4jRelation
from genpy.niha_thrift import Neo4jNode
from genpy.niha_thrift import Neo4jMemoryChunk
from genpy.niha_thrift.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

if __name__ == '__main__':
    # handler = Neo4jNode.Iface()
    # processor = Neo4jNode.Processor(handler)
    # handler1 = Neo4jRelation.Iface()
    # processor1 = Neo4jRelation.Processor(handler1)
    handler2 = Neo4jGraph.Iface()
    processor2 = Neo4jGraph.Processor(handler2)
    # handler3 = Neo4jMemoryChunk.Iface()
    # processor3 = Neo4jMemoryChunk.Processor(handler3)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9091)
    # transport1 = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    # transport2 = TSocket.TServerSocket(host='127.0.0.1', port=9092)
    # transport3 = TSocket.TServerSocket(host='127.0.0.1', port=9093)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # tfactory1 = TTransport.TBufferedTransportFactory()
    # pfactory1 = TBinaryProtocol.TBinaryProtocolFactory()
    # tfactory2 = TTransport.TBufferedTransportFactory()
    # pfactory2 = TBinaryProtocol.TBinaryProtocolFactory()
    # tfactory3 = TTransport.TBufferedTransportFactory()
    # pfactory3 = TBinaryProtocol.TBinaryProtocolFactory()

    # server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    # server1 = TServer.TSimpleServer(processor1, transport1, tfactory, pfactory)
    server2 = TServer.TSimpleServer(processor2, transport, tfactory, pfactory)
    # server3 = TServer.TSimpleServer(processor3, transport3, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    # print('Starting the Node server...')
    # server.serve()
    # print('done.')
    # print('Starting the Relation server...')
    # server1.serve()
    # print('done.')
    print('Starting the Graph server...')
    server2.serve()
    print('done.')
    #
    # print('Starting the MemoryChunk server...')
    # server3.serve()
    # print('done.')
