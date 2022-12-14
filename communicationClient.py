import socket
import threading

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = 2
    
    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
            self.status = 1
        except Exception as err:
            self.bridge.socketStateSig.emit(str(err))
            return

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

    def start(self):
        if self.status == 1:
            self.status = 0
            recieve_thread = threading.Thread(target=self.receive)
            recieve_thread.daemon = True
            recieve_thread.start()

    def write(self, message):
        if self.status == 0:
            print(message)
            data=f"{message}"
            self.sock.send(data.encode('utf-8'))

    def stop(self):
        if self.status == 1 or self.status == 0:
            self.status = 2
            self.sock.close()

    def requestDBFunc(self, client, context, request, data=None):
        if data is None:
            message = '35972^'+ str(context) + '^' + str(request)
        else:
            message = '35972^'+ str(context) + '^' + str(request) + '^' + '$'.join(data)
        self.write(message)


    def receive(self):
        self.sock.send(f"10351037&".encode('utf-8'))
        while self.status == 0:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                message.split('^')
                
                splitMessages = list(map( lambda x: str(x).split('$'),message.split('^')))
                for index, message in enumerate(splitMessages):
                    if len(message) == 1:
                        splitMessages[index] = message[0]
                self.bridge.DBmessageSig.emit(int(splitMessages[0]), splitMessages[1:])

            except Exception as err:
                #self.bridge.connectError.emit()
                self.bridge.socketStateSig.emit(str(err))
                #self.sock.close()
                break
        
