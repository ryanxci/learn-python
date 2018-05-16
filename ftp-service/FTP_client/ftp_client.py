import optparse
import socket

class ClientHandler:

    def __init__(self):
        self.op = optparse.OptionParser()

        self.op.add_option("-s","--server",dest="server")
        self.op.add_option("-P","--port",dest="port")
        self.op.add_option("-u","--username",dest="username")
        self.op.add_option("-p","--password",dest="password")

        options,args = self.op.parse_args()
        self.verify_args(options,args)
        self.make_connection()

    def verify_args(self,options,args):
        server=options.server
        port = options.port
        username = options.username
        password = options.pwssword

        if int(port)>0 and int(port)<65535:
            return True
        else:
            return False

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect()



