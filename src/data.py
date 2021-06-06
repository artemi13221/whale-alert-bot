from whaleapi import WhaleAPI

class data:
    #"transaction_type":"transfer" ==> 거래
    #"transaction_type":"burn" ==> 소각
    #unkown -> unkown의 데이터는 불필요.
    #usdt의 데이터도 중요함. usdt가 거래소로 이동한다는 것은 무엇인가를 사겠다는 의미
    #거래소로 입금 출금 위주의 데이터
    whale_api = WhaleAPI

    result = 0
    count = 0

    def __init__(self):
        pass