from whaleapi import WhaleAPI
import json

class data:
    #"transaction_type":"transfer" ==> 거래
    #"transaction_type":"burn" ==> 소각
    #unkown -> unkown의 데이터는 불필요.
    #usdt의 데이터도 중요함. usdt가 거래소로 이동한다는 것은 무엇인가를 사겠다는 의미할 수 있기 때문임.
    #거래소로 입금 출금 위주의 데이터를 필터링
    whale_api = WhaleAPI

    result = 0
    count = 0
    raw_data = None

    def get_raw_data():
        pass

    def check_transaction_type():
        pass

    def check_to_wallet():
        pass

    def check_from_wallet():
        pass

    def filtering_data():
        pass