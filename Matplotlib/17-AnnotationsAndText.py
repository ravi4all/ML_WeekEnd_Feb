import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style

import numpy as np
import urllib
import datetime as dt

#style.use('ggplot')
style.use('fivethirtyeight')
# print all the available styles
print(plt.style.available)
# print the location of matplotlib so that we can find styles and edit them
print(plt.__file__)

# fmt - format
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        a = b.decode(encoding)
        return strconverter(a)
    return bytesconverter

def graph_data(stock):

    fig = plt.figure()
    # ax1 is a subplot
    ax1 = plt.subplot2grid((1,1),(0,0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter = ',',
                                                          unpack = True,
                                                         converters={0: bytespdate2num('%Y%m%d')})

    x = 0
    y = len(date)
    # OHLC : open high low close
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1


    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    
    bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)

    # to display the last price
    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1]+4, closep[-1]), bbox=bbox_props)

    
##    # putting annotation...80% at x-axis and 90% at y-axis
##    # Annotation example with arrow
##    ax1.annotate('Good News', (date[11], highp[11]),
##                   xytext = (0.8, 0.9), textcoords='axes fraction',
##                 arrowprops = dict(facecolor='grey', color='grey'))
##
##    # Font dict example
##    font_dict = {'family' : 'serif',
##                 'color' : 'red',
##                 'size' : 15}
##    # Hard coded example
##    ax1.text(date[10], closep[1], 'Text Example', fontdict = font_dict)
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('STOCK')
    #plt.legend()
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data('ebay')
