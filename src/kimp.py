import requests
import datetime

#exchange_rate : 6H, upbit_price, binance_price : 1m
class Kimp:
    upbit_api_url = 'https://api.upbit.com/v1/ticker' #param = markets=
    binance_api_url = 'https://api.binance.com/api/v1/ticker/price' #param = symbol
    exchange_rate_api_url = 'https://api.ratesapi.io/api/latest?base=USD&symbols=KRW'
    requests_data = requests.get(upbit_api_url)

    def error_log(self, msg):
        pass

    def error_check(self):
        if self.requests_data.status_code != 200:
            print(str(datetime.date.ctime) + '[ERROR] errorcode : ' + str(self.requests_data.status_code))
        
        return self.requests_data.status_code
    
    def connect_url(self, url = '', params = None):
        if params == None:
            self.requests_data = requests.get(url)
        else:
            self.requests_data = requests.get(url=url, params=params)
        
        status_code = self.error_check()
        
        return status_code

    def get_exchange_rate(self): #갱신 주기 6h
        if (self.connect_url(url=self.exchange_rate_api_url)) == 200:
            return self.requests_data.json()['rates']['KRW']
        else:
            return 0

    def get_binance_price(self, symbol='BTC'): #갱신 주기 1m
        symbol = symbol + 'USDT'
        param = {'symbol':symbol}
        if (self.connect_url(url=self.binance_api_url, params=param)) == 200:
            return (float)(self.requests_data.json()['price'])
        else:
            return 0

    def get_upbit_price(self, symbol='BTC'): #갱신 주기 1m
        symbol = 'KRW-' + symbol
        param = {'markets':symbol}
        if (self.connect_url(url=self.upbit_api_url, params=param)) == 200:
            return self.requests_data.json()[0]['trade_price']
        else:
            return 0

    def cal_kimp(self, exchange_rate=0, binance_price=0, upbit_price=0): #실행 주기 1m
        result = 0
        if binance_price == 0 or upbit_price == 0:
            print(str(datetime.date.ctime) + ' - [ERROR] price data error! check api site or param(symbol).')
            result = 0
        elif exchange_rate == 0:
            print(str(datetime.date.ctime) + ' - [ERROR] exchage rate error! check api site.')
            result = 0
        else:
            result = ((upbit_price / (binance_price * exchange_rate )) * 100) - 100
        
        return result