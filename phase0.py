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
	#Retrieve the host, path and port of the url
	host, path, port = parse_url(url)
	P2tag = "u5780417_u5680607"
	return ("GET " + "{p} HTTP/1.1" + NL + "Host: {h}" + NL + "P2Tag: {t}" + NL + NL).format(p=path,h=host,t=P2tag)

def attack(url):
	#Retrieve the http_request from the function that makes it
	http_request = getreq(url)
	#get host and port (Necessary for making the connection)
	host, path, port = parse_url(url)
	#open socket, connect to host and port and then sent the request
	attack_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
	attack_socket.connect((host,port))
	attack_socket.send(http_request)

	content_to_load = ""
	head =""
	while '\r\n\r\n' not in head:
		buf = attack_socket.recv(1)
		head += buf
	return head

print attack("http://10.27.8.20:8080/primes11.txt")


# #number of requests to be made:
# numreq = sys.argv[2]
# #max concurrent requests that can be made at once:
# maxConcurrent = sys.argv[-2]
# #Url to be attacked
# url = sys.argv[-1]