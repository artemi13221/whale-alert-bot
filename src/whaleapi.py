import json
import requests
import os
import time

class WhaleAPI:
    api_key = os.environ['API_KEY']
    url = "https://api.whale-alert.io/v1"
    r = requests.get(url)
    t = int(time.time())
            
    def errorCheck(self):
        if self.r.status_code != 200:
            print('[ERROR] errorcode : ' + str(self.r.status_code))
        

    def connectURL(self, addUrl='', params={}):
        param = {'api_key':self.api_key}
        params.update(param)
        tmpUrl = self.url + '/' + addUrl

        self.r = requests.get(tmpUrl, params=params)
        self.errorCheck()

    def getStatus(self):
        self.connectURL(addUrl='status')

    def getTransactions(self, start = t, end = t-60, cursor=None, limit=100):
        params = {'start' : start, 'end' : end, 'min_value' : 500000}
        if cursor != None:
            params['cursor'] = cursor
        
        if limit < 100:
            params['limit'] = limit
        
        self.connectURL(addUrl='transactions', params=params)