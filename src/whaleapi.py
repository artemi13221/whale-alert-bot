import json
import requests
import os
import time

class WhaleAPI:
    api_key = os.environ['API_KEY']
    url = "https://api.whale-alert.io/v1"
    requestData = requests.get(url)
    now_timestamp = int(time.time())
            
    def errorCheck(self):
        if self.requestData.status_code != 200:
            print('[ERROR] errorcode : ' + str(self.requestData.status_code))
        

    def connectURL(self, addUrl='', params={}):
        param = {'api_key':self.api_key}
        params.update(param)
        tmpUrl = self.url + '/' + addUrl

        self.requestData = requests.get(tmpUrl, params=params)
        self.errorCheck()

    def getStatus(self):
        self.connectURL(addUrl='status')

        return self.requestData.text

    def getTransactions(self, start = now_timestamp, end = now_timestamp-60, cursor=None, limit=100):
        params = {'start' : start, 'end' : end, 'min_value' : 500000}
        if cursor != None:
            params['cursor'] = cursor
        
        if limit < 100:
            params['limit'] = limit
        
        self.connectURL(addUrl='transactions', params=params)

        return self.requestData.text