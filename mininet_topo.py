#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info, warn
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

class customTopo(Topo):
    """create topology with numCore core switches
    numEdge edge switches, hostsPerEdge, bw bandwidth, delay"""
    
    coreSwitcheList = []
    edgeSwitcheList = []
    hostList = []
    linkList = {}

    def build(self, numCores = 3, numEdges=5, hostsPerEdge=2, bw = 5, delay = None):
        #Write tree construction here
        

def perfTest():
    topo = customTopo()
    net = Mininet(topo=topo, link=TCLink, controller=None)
    

    print "start RYU controller"
    raw_input()

    net.addController('rmController', controller=RemoteController,
                      ip='127.0.0.1', port=6633)
    net.start()

    print "Testing network connectivity"
    net.pingAll()
    dumpNodeConnections(net.hosts)
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    CLI(net)
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
