import datetime

import matplotlib.pyplot as plt
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


x = [0]
y = [0]
x1 = [0]
y1 = [0]

f, axx = plt.subplots(2)


# plot the price of crypto currency
def plot_values(to_symbol):
    i = 0
    while (True):
        data = get_price_data(to_symbol, ['USD', 'PKR'])
        i += 1
        x.append(i)
        y.append(data['USD'])
        y1.append(data['PKR'])
        axx[0].set_title(to_symbol + " Vs USD, Last updated at: " + str(datetime.datetime.now()))
        axx[0].plot(x, y)
        axx[1].set_title(to_symbol + " Vs PKR, Last updated at: " + str(datetime.datetime.now()))
        axx[1].plot(x, y1)
        plt.pause(1)


plot_values('BTC')
