import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24, 12, 33, 11, 111712),
    datetime(2019, 5, 25, 12, 33, 11, 123913),
    datetime(2019, 5, 26, 12, 33, 11, 145914),
    datetime(2019, 5, 27, 12, 33, 11, 187955),
    datetime(2019, 5, 28, 12, 33, 11, 299976),
    datetime(2019, 5, 29, 12, 33, 11, 333990),
    datetime(2019, 5, 30, 12, 33, 11, 444999)
]


dates_str = [dt.strftime('%Y-%m-%d-%H:%M:%S.%f') for dt in dates]


y = [0, 1, 3, 4, 6, 5, 7]

with plt.style.context(['science', 'grid', 'no-latex']):
    dates = mpl_dates.datestr2num(dates_str)  # convert string dates to numbers
    # plt.plot_date(dates, y, linestyle='solid')
    plt.plot(dates, y)
    plt.gcf().autofmt_xdate()

    date_format = mpl_dates.DateFormatter(
        '%Y_%m_%d_%H_%M_%S_%f')  # custom date formatter
    # date_format = mpl_dates.DateFormatter(
    #     '%M_%S_%f')  # custom date formatter

    plt.gca().xaxis.set_major_formatter(date_format)  # custom date formatter
    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    plt.tight_layout()

    plt.show()
