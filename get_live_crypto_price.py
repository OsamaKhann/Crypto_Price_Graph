import datetime

import matplotlib.pyplot as plt
import requests


# simply fetechs data from given api and return result in json from
def get_price_data(from_symbol, to_symbols='USD', exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(from_symbol.upper(),
                                                                                 ','.join(to_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data


# plot the price of crypto currency
def plot_values(to_symbol):
    i = 0
    while (True):
        data = get_price_data(to_symbol)
        i += 1
        x.append(i)
        y.append(data['USD'])
        plt.title(to_symbol + " Vs USD, Last updated at: " + str(datetime.datetime.now()))
        plt.plot(x, y)
        fig.canvas.draw()
        plt.pause(1000)


x = [0]
y = [0]
fig = plt.gcf()
fig.show()
fig.canvas.draw()
plt.ylim([0, 15000])

plot_values('BTC')
