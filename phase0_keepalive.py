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
    head=''
    fail_count=0
    #Retrieve the http_request from the function that makes it
    http_request = getreq(url)
    #get host and port (Necessary for making the connection)
    host, path, port = parse_url(url)
    #open socket, connect to host and port and then sent the request
    attack_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    attack_socket.settimeout(0.3)
    try:
        attack_socket.connect((host,port))
    except skt.error,e:
        fail_count+=1
        pass
    except skt.timeout:
        fail_count += 1
        pass

    times = float(numreq)/maxCon
    start = time.time()
    pass_counter = 0
    tottime=0
    for i in range(int(times)):
        for j in range(maxCon):
            start=time.time()
            try:
                attack_socket.send(http_request)
                pass_counter+=1
            except skt.error, e:
                fail_count +=1
                continue
            except skt.timeout:
                fail_count += 1
                continue
            # while '\r\n\r\n' not in head:
            #     buf = attack_socket.recv(1024)
            #     head += buf
            # content.append(head)
            end = time.time()
            tottime += (end-start)
    if (pass_counter + fail_count) != numreq:
        for k in range((numreq-(pass_counter + fail_count))):
            start=time.time()
            try:
                attack_socket.send(http_request)
                pass_counter+=1
            except skt.timeout:
                fail_count+=1
            except skt.error, e:
                fail_count +=1
                continue
            # while '\r\n\r\n' not in head:
            #     buf = attack_socket.recv(1)
            #     head += buf
            # pass_counter +=1
            end = time.time()
            tottime += end-start

    attack_socket.close()
    # return pass_counter, fail_count, tottime
    print "Replies from the server: ", head
    print "Time taken for tests: ", tottime," seconds" 
    print "Completed requests: ", pass_counter
    print "Failed requests: ", fail_count
    print "Avg requests per second: ", float(numreq)/tottime," [req/s]"

url = "http://10.27.8.20:2201/"
numreq = 10
maxCon = 2
attack(url,numreq,maxCon)

