import mysql.connector
from mysql.connector import Error
class connect2MySql:
    def __init__(self, username, password, hostLocation, databaseName):
        self.user=username
        self.password=password
        self.host=hostLocation
        self.database=databaseName
        self.connected=mysql.connector.connect(user=username
                                               , password=password
                                               , host=hostLocation
                                               , database=databaseName)

    def checkConnection(self):
        if self.connected.is_connected():
            print('sever version --> ', self.connected.get_server_info())
            return 'connect successfully'
        else:
            return 'fail to connect'

    def createCursor(self):
        print('.'*10, 'creating the connection', '.'*10)
        self.cursorObj= self.connected.cursor()
        return self.cursorObj

    def showCursor(self):
        return self.cursorObj

    def reConnection(self):
        self.connected=mysql.connector.connect(user=self.user
                                               , host=self.host
                                               , password=self.password
                                               , database=self.database)

    def changeConnection(self, changeName : tuple, changeValue : tuple):
        """
        this allows clients change the details of connection
        such as Username, Password, Host, Database
        """
        print('.'*10,'changing the connection...','.'*10)
        coupleChange=tuple(zip(changeName, changeValue))
        name=('host', 'user', 'password', 'database')
        for i in coupleChange:
            if i[0] in name:
                self.__dict__[i[0]]=i[1]
        print('.'*10,'reconnecting the connection','.'*10)
        self.reConnection()
        print('.'*10,'reconnected','.'*10)

    def __repr__(self):
        x1=f"username = {self.user}\n"
        x2=f"password = {self.password}\n"
        x3=f"host = {self.host}\n"
        x4=f"database = {self.database}"
        return x1+x2+x3+x4

    def close(self):
        self.connected.clse()
