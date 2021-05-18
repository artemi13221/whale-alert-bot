import requests
import json

class Kimp:
    upbit_api_url = 'https://api.upbit.com/v1/ticker' #param = markets=
    binance_api_url = 'https://api.binance.com/api/v1/ticker/price' #param = symbol
    exchange_rate_api_url = ''
    symbols = ['BTC', 'ETH', 'DOGE']
    requests_data = requests.get()

    def error_log(self):
        pass

    def error_check(self):
        if self.requests_data != 200:
            print('[ERROR] errorcode : ' + str(self.requests_data.status_code))
    
    def connect_url(self, url = '', params = None):
        if params == None:
            self.requests_data = requests.get(url)
        else:
            self.requests_data = requests.get(url=url, params=params)
        
        self.error_check()

    def get_exchange_rate(self):
        pass

    def get_binance_price(self, symbol):
        symbol = symbol + 'USDT'
        param = {'symbol':symbol}
        self.connect_url(url=self.binance_api_url, params=param)

        if self.requests_data.status_code == 200:
            return (int)(self.requests_data.json()['price'])
        else:
            return 0

    def get_upbit_price(self, symbol):
        symbol = 'KRW-' + symbol
        param = {'markets':symbol}
        self.connect_url(url=self.upbit_api_url, params=param)

        if self.requests_data.status_code == 200:
            return self.requests_data.json()['trade_price']
        else:
            return 0

    def cal_kimp(self, symbol):
        pass