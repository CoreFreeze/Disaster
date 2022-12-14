import socketserver
import threading
from time import sleep
import queue
import DBHandler

class chatTCPHandler(socketserver.BaseRequestHandler):

    def setup(self) -> None:
        self.server.addClients(self)
        return super().setup()

    def finish(self) -> None:
        self.server.removeClients(self)
        return super().finish()

    def handle(self):
        message = self.request.recv(1024).decode('utf-8')
        # 서버에 표시
        #print(message)
        splitedMessage =  str(message).split('&')
        # 서버 접속 행동 X
        # 서버에 등록만
        # 0 & 지역번호
        if splitedMessage[0] == '10351037':
            # 예외 처리 
            if splitedMessage[0] == message:
                return
            while True:
                try:
                    message = self.request.recv(1024).decode('utf-8')
                    # 서버에 표시
                    splitedMessage =  str(message).split('^')
                    if splitedMessage[0] == '35972':
                        if len(splitedMessage) > 3:
                            self.server.requestDBFunc(client=self, context=int(splitedMessage[1]), request=int(splitedMessage[2]),data = splitedMessage[3].split('$'))
                        else:
                            self.server.requestDBFunc(client=self, context=int(splitedMessage[1]), request=int(splitedMessage[2]), data=None)
                    else:
                        break

                except Exception as err:
                    break



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    request_queue_size = 10
    daemon_threads = True

    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass,True)
        self.clients = []
        self.q = queue.Queue()
        thread = threading.Thread(target=self.process_DB_Request)
        thread.daemon = True
        thread.start()

    def addClients(self, client):
        self.clients.append(client)

    def removeClients(self, client):
        self.clients.remove(client)

    def requestDBFunc(self, client, context, request, data):
        self.q.put((client, context, request, data))
    
    def process_DB_Request(self):
        while True:
            requestData = self.q.get()

            myDB = DBHandler.sqlDB()
            functionList = [myDB.insertTag, myDB.searchTags, myDB.searchTag, myDB.searchTagFromDate, myDB.modifyTag, myDB.deleteTag, \
                        myDB.searchProgramNameList, myDB.searchProgramNameWeekList, myDB.searchProgramNameWeekendList, myDB.searchProgram, myDB.insertProgram, \
                        myDB.modifyProgram, myDB.deleteProgram, myDB.searchSpotNameList, myDB.searchSpot, myDB.insertSpot, \
                        myDB.modifySpot, myDB.deleteSpot, myDB.searchBroadcastDate, myDB.searchBroadcastList, myDB.insertDisaster, myDB.createTabele, \
                        myDB.searchDisaster, myDB.modifyDisaster, myDB.deleteDisaster, myDB.searchBroadcastDateWithProgram]

            if requestData[3] is not None:
                retData = self._requestDBFunc(functionList[requestData[2]], *requestData[3])
            else:
                retData = self._requestDBFunc(functionList[requestData[2]])

            myDB.closeDB()

            if retData is not None:
                if requestData[0] is not None:
                    data = [str(requestData[1])]
                    for tupleData in retData:
                        if isinstance(tupleData, tuple):
                            tupleData = map(str, tupleData)
                            linkedData = '$'.join(tupleData)
                            data.append(linkedData)
                        else:
                            data.append(str(tupleData))
                    
                    data = f"{'^'.join(data)}".encode('utf-8')
                    requestData[0].request.send(data)
                else:
                    self.bridge.DBmessageSig.emit(requestData[1], retData)

    def _requestDBFunc(self, func, *requestData):
        return func(*requestData)





if __name__ == "__main__":

    HOST = '127.0.0.1'
    PORT = 9090

    server = ThreadedTCPServer((HOST,PORT), chatTCPHandler, 4)
    server.serve_forever()
