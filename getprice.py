import requests

def get_coin_price(coin_id):

    url = "https://api.coingecko.com/api/v3/simple/price"

    # Solicita o ID da moeda do usuário
    #coin_id = input("Digite o ID da moeda que você quer verificar o preço: ")

    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "YOUR KEY"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if coin_id in data:
            coin_price_usd = data[coin_id]["usd"]
            print(f"Preço do {coin_id.upper()} (USD): {coin_price_usd}")
            return coin_price_usd
        else:
            print("Moeda não encontrada.")
            return None
    else:
        print("Falha ao recuperar dados:", response.status_code)
        return None
