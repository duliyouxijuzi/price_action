import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",  # 指定加密货币
        "vs_currencies": "usd"  # 指定法币，USD 表示美元
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        btc_price = data['bitcoin']['usd']
        print(f"当前BTC价格: ${btc_price}")
        return btc_price
    except requests.exceptions.RequestException as e:
        print(f"获取价格时发生错误: {e}")
        return None

if __name__ == "__main__":
    get_btc_price()
