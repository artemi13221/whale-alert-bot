import datetime
import requests
import os
import dotenv
import json

class Slack:
    dotenv.load_dotenv(verbose=True)
    api_key = os.environ.get('SLACK_API_KEY')
    channel_name = None
    channel_id = None

    def set_channel(self, name):
        url = 'https://slack.com/api/conversations.list'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization':'Bearer ' + str(self.api_key)
        }

        channel_data = requests.post(url=url, headers=headers).json()
        if channel_data['ok'] != True:
            return False

        for i in channel_data['channels']:
            if i['name'] == name:
                self.channel_id = i['id']
                self.channel_name = i['name']
                return True
        
        return False
    
    def send_msg(self, transaction):
        url = 'https://slack.com/api/chat.postMessage'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization':'Bearer ' + str(self.api_key)
        }
        
        if self.channel_id == None:
            print('[Error] - Please set channel')
            return False
        
        blocks_date = datetime.datetime.ctime(datetime.datetime.now())
        blocks_coin = {
            'symbol': transaction['symbol'],
            'amount': transaction['amount'],
            'amount_usd': transaction['amount_usd'],
            'to_owner': transaction['to']['owner'],
            'from_owner':transaction['from']['owner']
        }
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":whale: Whale Alert :whale:"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "text": "*" + blocks_date + "*  |  whale-alert",
                        "type": "mrkdwn"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*₿ " + str(blocks_coin['amount']) + " #" + str(blocks_coin['symbol']) + "* ($" + str(blocks_coin['amount_usd']) + ")"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "* #" + str(blocks_coin['from_owner']) + " → #" + str(blocks_coin['to_owner']) + "*"
                }
            }
        ]
        
        params = {
            'channel': self.channel_id,
            'blocks': json.dumps(blocks)
        }

        msg_data = requests.post(url=url, headers=headers, params=params).json()

        print(msg_data)

        if msg_data['ok'] == False:
            print("[Error] - " + blocks_date + " - POST Err.")
            return False
        
        return True