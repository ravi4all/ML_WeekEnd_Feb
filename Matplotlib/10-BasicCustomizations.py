import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

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

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'

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
                                                          converters = {0: bytespdate2num('%Y%m%d')})

    ax1.plot_date(date, closep, '-', label = 'Price')
    
    for label in ax1.xaxis.get_ticklabels():
        # To rotate the date label
        label.set_rotation(45)
    # to insert the grid on graph
    #ax1.grid(True, color='g', linestyle='-', linewidth=5)
    ax1.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Graphs')
    plt.legend()
    # It will adjust the subplot and manage the paddings
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data('FB')
