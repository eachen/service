#--*coding:utf-8*--

'''
Created on 2016��8��17��

@author: pc  one
'''
import threading
import socket
class service(threading.Thread):
    def __init__(self):
        print 'open service'

    def startService(self):
        skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        skt.bind(('0.0.0.0',9999))
        skt.listen(5)
        while True:
            cl_skt,addr=skt.accept()
            print cl_skt
            print addr
            t=threading.Thread(target=self.sendMsg,args=(cl_skt,))
            t.start()
    def sendMsg(self,skt):
        skt.send("hell,client")
        while True:
            print skt.recv(1024)
            
    def run(self):
        self.startService()
        
service().run()
    