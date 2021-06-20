import requests
import os
import time
import datetime

class WhaleAPI:
    api_key = os.environ['WHALE_API_KEY']
    url = "https://api.whale-alert.io/v1"
    request_data = None
    now_timestamp = int(time.time())
    
    def error_log(self, msg):
        pass
            
    def error_check(self):
        if self.request_data.status_code != 200:
            print(str(datetime.date.ctime) + ' - [ERROR] errorcode : ' + str(self.request_data.status_code)) 

        return self.requests_data.status_code

    def connect_url(self, addUrl='', params={}):
        param = {'api_key':self.api_key}
        params.update(param)
        tmpUrl = self.url + '/' + addUrl

        self.request_data = requests.get(tmpUrl, params=params)
        status_code = self.error_check()

        return status_code

    def get_status(self):
        self.connect_url(addUrl='status')

        return self.request_data.json()

    def get_transactions(self, start=now_timestamp, cursor=None, limit=100):
        params = {'start': start, 'min_value': 500000}
        if cursor != None:
            params['cursor'] = cursor
        
        if limit < 100:
            params['limit'] = limit
        
        self.connect_url(addUrl='transactions', params=params)

        return self.request_data.json()