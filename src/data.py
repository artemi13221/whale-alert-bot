from whaleapi import WhaleAPI
import json
import time

class data:
    #'transaction_type':'transfer' ==> 거래
    #'transaction_type':'burn' ==> 소각
    #unkown -> unkown의 데이터는 불필요.
    #usdt의 데이터도 중요함. usdt가 거래소로 이동한다는 것은 무엇인가를 사겠다는 의미할 수 있기 때문임.
    #거래소로 입금 출금 위주의 데이터를 필터링
    whale_api = WhaleAPI
    raw_data = None
    result_data = None

    def check_transaction_type(self, t):
        return (t['transaction_type]'] == 'transfer' or t['transaction_type]'] == 'burn')

    def check_to_wallet(self, t):
        return t['to']['owner_type'] != 'unknown'

    def check_from_wallet(self, t):
        return t['from']['owner_type'] != 'unknown'

    def filtering_data(self):
        self.result_data = []
        for t in self.raw_data['transactions']:
            if self.check_transaction_type and (self.check_from_wallet or self.check_to_wallet):
                self.result_data.append(t)

    def get_data(self, start, cursor=None, limit=None):
        self.raw_data = self.whale_api.get_transactions(start=start)

        if self.raw_data['result'] != 'success' :
            print('[Error] : timestamp : ' + str(int(time.time())) + 'error code : ' + self.raw_data['result'])
            return
        
        self.filtering_data()