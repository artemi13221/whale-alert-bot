from src import slack
from src import data

transaction = {
    "blockchain": "ethereum",
    "symbol": "eth",
    "id": "1632622009",
    "transaction_type": "transfer",
    "hash": "3432e81f21dfc0c75ca04458d131e1f173e6d66975d675b7e734e01e8430bff8",
    "from": {
    "address": "876eabf441b2ee5b5b0554fd502a8e0600950cfa",
    "owner": "bitfinex",
    "owner_type": "exchange"
    },
    "to": {
    "address": "742d35cc6634c0532925a3b844bc454e4438f44e",
    "owner": "bitfinex",
    "owner_type": "exchange"
    },
    "timestamp": 1624315202,
    "amount": 11655.588,
    "amount_usd": 21949700,
    "transaction_count": 1
}

# kimp_data = kimp.Kimp()
slack_bot = slack.Slack()
transaction_data = data.Data()

# exchange_rate = kimp_data.get_exchange_rate()
# upbit_price = kimp_data.get_upbit_price()
# binance_price = kimp_data.get_binance_price()

slack_bot.set_channel('bot-coin-whale-alert')
slack_bot.send_msg(transaction=transaction)