import requests


# simply fetechs data from given api and return result in json from
def get_price_data(from_symbol, to_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(from_symbol.upper(),
                                                                                 ','.join(to_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data


bitcoin_data = get_price_data('BTC', ['ETH', 'USD', 'PKR'])
print(bitcoin_data)
