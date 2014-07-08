#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SocketServer
import threading
import subprocess
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
# def fun(param1, param2):
#     return param1 + param2
# class MyRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer):
#     def __init__(self, *args, **kwargs):
#         SimpleXMLRPCServer.__init__(self, *args, **kwargs)

# cmds = ['python', '/home/xinyuan/mysource/python/cola/process/testrpc.py']
# subprocess.Popen(cmds)
if __name__ == "__main__":
#     rpc_server = MyRPCServer(('127.0.0.1', 11103))
#     thd = threading.Thread(target=rpc_server.serve_forever)
#     # thd.setDaemon(True)
#     thd.start()
#     rpc_server.register_function(fun)
    s = xmlrpclib.ServerProxy('http://127.0.1.1:11103')
    print s.start_job('wiki', False)