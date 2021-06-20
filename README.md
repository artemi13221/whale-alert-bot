<!-- Heading -->
# Whale alert BOT
고래의 데이터를 수집하여 분류하고 실시간으로 슬랙을 통해 보내주는 봇
> 고래는 큰 액수의 코인이 다른 지갑으로 이송되는 경우를 말합니다.

## 이용방법
이 봇은 [whale-alert.io](https://whale-alert.io/)의 API를 활용하므로, API키가 필요합니다.
.env 파일을 생성하고 아래와 같이 입력하신 뒤,
```
WHALE_API_KEY=<here>
```
\<here>부분에 [whale-alert.io](https://whale-alert.io/pricing) 사이트에서 발급받으신 API키를 입력해주세요.
그 뒤, core.py를 실행하여 봇을 가동합니다.