'''
方法一 -> 轉字串
當1的方案使用的不順手，例如設定%f，硬是要出現到微秒
但是你只需要到毫秒時，就可以參考這個script
基本上就是繞過matplotlib，自己把time axis sorting之後，取出自己要的作為字串
然後以字串的方式上xtick

方法二 -> 自訂DataFormatter



'''

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
################# 方法二 ######################
import matplotlib.ticker as ticker


class PrecisionDateFormatter(ticker.Formatter):
    """
    Extend the `matplotlib.ticker.Formatter` class to allow for millisecond
    precision when formatting a tick (in days since the epoch) with a
    `~datetime.datetime.strftime` format string.

    """

    def __init__(self, fmt, precision=3, tz=None):
        """
        Parameters
        ----------
        fmt : str
            `~datetime.datetime.strftime` format string.
        """
        from matplotlib.dates import num2date
        if tz is None:
            from matplotlib.dates import _get_rc_timezone
            tz = _get_rc_timezone()
        self.num2date = num2date
        self.fmt = fmt
        self.tz = tz
        self.precision = precision

    def __call__(self, x, pos=0):
        if x == 0:
            raise ValueError("DateFormatter found a value of x=0, which is "
                             "an illegal date; this usually occurs because "
                             "you have not informed the axis that it is "
                             "plotting dates, e.g., with ax.xaxis_date()")

        dt = self.num2date(x, self.tz)
        ms = dt.strftime("%f")[:self.precision]

        return dt.strftime(self.fmt).format(ms=ms)

    def set_tzinfo(self, tz):
        self.tz = tz


dates_str = [dt.strftime('%Y-%m-%d-%H:%M:%S.%f') for dt in dates]
y = [0, 1, 3, 4, 6, 5, 7]


with plt.style.context(['science', 'grid', 'no-latex']):
    dates = mpl_dates.datestr2num(dates_str)  # convert string dates to numbers
    # plt.plot_date(dates, y, linestyle='solid')
    plt.plot(dates, y)
    plt.gcf().autofmt_xdate()

    # date_format = mpl_dates.DateFormatter(
    #     '%M_%S_%f')  # custom date formatter
    plt.gca().xaxis.set_major_formatter(
        PrecisionDateFormatter(fmt="%M:%S.{ms}", precision=1))
    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    plt.tight_layout()

    plt.show()


################# 方法一 ######################
# def get_min_second_ms(dt: datetime) -> str:
#     return dt.strftime('%m:%S.%f')[:-3]


# dates_str = [dt.strftime('%Y-%m-%d-%H:%M:%S.%f') for dt in dates]
# min_second_ms = [get_min_second_ms(dt) for dt in dates]

# y = [0, 1, 3, 4, 6, 5, 7]


# with plt.style.context(['science', 'grid', 'no-latex']):

#     plt.plot(np.arange(len(y)), y)  # 只畫value

#     plt.xticks(np.arange(len(min_second_ms)),
#                min_second_ms, rotation=30)  # 以字串來畫ticks
#     plt.title('Bitcoin Prices')
#     plt.xlabel('Time')
#     plt.ylabel('Closing Price')
#     plt.tight_layout()
#     plt.show()
