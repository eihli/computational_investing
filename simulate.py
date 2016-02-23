import numpy as np
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import datetime as dt
import math

def run(dt_start, dt_end, ls_symbols, alloc):
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    c_dataobj = da.DataAccess('Yahoo')
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    na_price = d_data['close'].values
    na_normalized_prices = na_price / na_price[0, :]
    na_daily_returns = tsu.returnize0(na_normalized_prices.copy())
    na_allocated_daily_ret = na_daily_returns * alloc
    print 'Allocated-Adjusted Daily Returns'
    print na_allocated_daily_ret
    na_total_daily_ret = np.sum(na_allocated_daily_ret, 1)
    print 'Total Daily Returns: '
    print na_total_daily_ret
    std_dev = np.std(na_total_daily_ret)
    print 'Standard Deviation (Vol): ' + str(std_dev)
    avg_daily_ret = np.average(na_total_daily_ret)
    print 'Average Daily Return: ' + str(avg_daily_ret)
    sharpe = calc_sharpe_ratio(avg_daily_ret, std_dev)
    print 'Sharpe: ' + str(sharpe)
    cum_ret = calc_cum_return(na_total_daily_ret)
    print 'Cumulative Return: ' + str(cum_ret)
    return std_dev, avg_daily_ret, sharpe, cum_ret

def calc_std_dev(population):
    return np.std(population)

def calc_avg_daily_return(returns):
    avg_daily_return = 1
    for i in range(len(returns)):
        avg_daily_return *= 1 + returns[i]
    return avg_daily_return - 1

def calc_sharpe_ratio(avg_daily_ret, std_dev):
    k = math.sqrt(250)
    return k * avg_daily_ret / std_dev

def calc_cum_return(returns):
    return reduce(lambda x, y: (1+x) * (1+y) - 1, returns)

