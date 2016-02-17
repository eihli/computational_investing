import numpy as np
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import math

def run(dt_start, dt_end, symbols):
    dt_start = dt.datetime(2006, 01, 01)
    dt_end = dt.datetime(2010, 12, 31)
    pass

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
    dt_start = dt.datetime(*map(int, start_date.split('/')))
    dt_end = dt.datetime(*map(int, end_date.split('/')))
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    c_dataobj = da.DataAccess('Yahoo')
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    return ldf_data
