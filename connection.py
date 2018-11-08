import json
import time

class Connection():
    ip = ""
    port = 3333
    connectionTimestamp = 0

    # 10 minutes timeout connection
    _connectionTimeout = 60 * 10

    def __init__(self, addrTuple, connectionTimestamp):
        self.ip, self.port = addrTuple
        self.connectionTimestamp = connectionTimestamp

    def getAddress(self):
        return self.ip, self.port

    def getConnectionTimestamp(self):
        return self.connectionTimestamp

    def setConnectionTimestamp(self, newConnectionTimestamp):
        self.connectionTimestamp = newConnectionTimestamp

    def isOutdatedConnection(self):
        return self.getConnectionTimestamp() < time.time() - self._connectionTimeout

    def getAsDict(self):
        return {
            "ip" : self.ip,
            "port" : self.port,
            "lastConnection" : self.connectionTimestamp
        }

    def getJson(self):
        return json.dumps(self.getAsDict(), ensure_ascii=False).encode()


class ConnectionsList():
    __list = []

    def addToList(self, connection):
        if self.isConnectionInList(connection):
            self.removeFromList(connection)
        self.__list.append(connection)

    def removeFromList(self, connection):
        for index, c in enumerate(self.__list):
            if c.getAddress() == connection.getAddress():
                self.__list = self.__list[:index] + self.__list[index+1:]
                return

    def isConnectionInList(self, connection):
        for c in self.__list:
            if c.getAddress() == connection.getAddress():
                return True
        return False

    def clearOutdatedItems(self):
        for c in self.__list:
            if c.isOutdatedConnection():
                self.removeFromList(c)

    def getListJson(self):
        self.clearOutdatedItems()
        return json.dumps(self.__list, default=lambda o: o.getAsDict(), ensure_ascii=False).encode()
