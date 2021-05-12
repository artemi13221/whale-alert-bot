import json
import requests

class WhaleAPI:
    api_key = 123
    url = "https://api.whale-alert.io/v1"
    status = "status"
    transactions = "transactions"
    r = requests.get(url)

    def __init__(self):
        self.errorCheck()
            
    def errorCheck(self):
        if self.r.status_code != 200:
            print('[ERROR] API server is down. errorcode : ' + str(self.r.status_code))
        
        return self.r.status_code

    def connectURL(self, params):
        self.r = requests(self.url, params=params)

        self.errorCheck()
            
    def getStatus(self):
        pass

    def getTransactions(self, start, end):
        pass

    def getTransactions(self, start, end, cursor):
        pass

    def getTransactions(self, start, end, cursor, limit):
        pass
    
    def checkStatus(self):
        pass
    