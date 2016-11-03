import sys
from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.ioloop import IOLoop
import collections
import itertools
import time
from urlparse import urlparse

if __name__ == '__main__':
    input = sys.argv
    # url = input[-1]
    numReq = 500
    url = "http://10.27.8.20:8080/"
    #url = "http://10.27.8.20:8080/"
    # nummconn = int(input[4])
    maxConn = 100
    global completed_request
    global i
    NL = "\r\n"
    lst=[]
    # completed_request = collections.Counter()
    completed_request = itertools.count(0)
    # print nummconn
    # nummreq = int(input[2])
    

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

def handle_request(response):
    lst.pop()
    if len(lst) == 0:
        IOLoop.instance().stop()
    completed_request.next()
    # completed_request.update({str(response.code):1})

# request = getreq()
http_client = CurlAsyncHTTPClient(None, max_clients=maxConn)

for iteration in xrange(numReq):
  http_client.fetch(getreq(url), handle_request)
  lst.append("1")
IOLoop.instance().start()


print "Completed requests: " + str(next(completed_request))
print "Failed requests: " + str(numReq - (next(completed_request)-1))
print "Total Request = " +str(numReq)