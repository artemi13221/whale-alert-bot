import json
import requests
import os

class WhaleAPI:
    api_key = os.environ['API_KEY']
    url = "https://api.whale-alert.io/v1"
    r = requests.get(url)
            
    def errorCheck(self):
        if self.r.status_code != 200:
            print('[ERROR] errorcode : ' + str(self.r.status_code))
        
        return self.r.status_code

    def connectURL(self, addUrl='', params={}):
        param = {'api_key':self.api_key}
        params.update(param)
        tmpUrl = self.url + '/' + addUrl

        self.r = requests.get(tmpUrl, params=params)
        self.errorCheck()

    def getStatus(self):
        self.connectURL()

    def getTransactions(self, start, end):
        pass

    def getTransactions(self, start, end, cursor):
        pass

    def getTransactions(self, start, end, cursor, limit):
        pass
    
    def checkStatus(self):
        pass
    