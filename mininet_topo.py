#!/usr/bin/python

#Copyright (c) 2016 Enrique Saurez

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info, warn
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.util import dumpNodeConnections

class customTopo(Topo):
    """create topology with numCore core switches
    numEdge edge switches, hostsPerEdge, bw bandwidth, delay"""
    
    def build(self, numCores = 3, numEdges=5, hostsPerEdge=2, bw = 5, delay = None):
        #Write tree construction here
        

def test():
    topo = customTopo()
    net = Mininet(topo=topo, link=TCLink, controller=None)
    

    print "start RYU controller"
    raw_input()

    net.addController('rmController', controller=RemoteController,
                      ip='127.0.0.1', port=6633)
    net.start()

    print "Testing network connectivity"
    net.pingAll()
    #dumpNodeConnections(net.hosts)
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    CLI(net)
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    test()
