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
    print na_allocated_daily_ret[:10]
    na_total_daily_ret = np.sum(na_allocated_daily_ret, 1)
    print 'hi'
    print na_total_daily_ret[:10]
    std_dev = np.std(na_total_daily_ret)
    print std_dev
    avg_daily_ret = np.average(na_total_daily_ret)
    print avg_daily_ret
    sharpe = calc_sharpe_ratio(avg_daily_ret, std_dev)
    print sharpe
    return 1, std_dev, 3, 4

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

def get_stocks_dataframe(start_date, end_date, ls_symbols):
    dt_start = dt.datetime(*start_date.split('/'))
    dt_end = dt.datetime(*end_date.split('/'))
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    c_dataobj = da.DataAccess('Yahoo')
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    return ldf_data
