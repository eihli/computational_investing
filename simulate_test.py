import unittest
import datetime as dt
import simulate as sim

class Simulate(unittest.TestCase):

    def test_has_run_function(self):
        self.assertTrue(hasattr(sim, 'run'))

    def test_calculates_standard_deviation(self):
        population = [3, 5, 1, 3]
        std_dev = sim.calc_std_dev(population)
        self.assertAlmostEqual(1.41, std_dev, 2)

    def test_calc_avg_daily_return(self):
        returns = [.009, -.007, .008]
        avg_daily_returns = sim.calc_avg_daily_return(returns)
        self.assertAlmostEqual(.00995, avg_daily_returns, 5)

    def test_calc_sharpe_ratio(self):
        returns = [.009, -.007, .008]
        avg_daily_return = sim.calc_avg_daily_return(returns)
        std_dev = sim.calc_std_dev(returns)
        print avg_daily_return
        print std_dev
        sharpe_ratio = sim.calc_sharpe_ratio(avg_daily_return, std_dev)
        print sharpe_ratio
        self.assertAlmostEqual(sharpe_ratio, 21.5, 2)

#   def test_get_stocks_dataframe(self):
#      ls_symbols = ["AAPL", "GOOG"]
#      df = sim.get_stocks_dataframe("2006/01/01", "2006/01/05", ls_symbols)

    def test_run(self):
        dt_start = dt.datetime(2011, 01, 01)
        dt_end = dt.datetime(2011, 12, 31)
        ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
        alloc = [0.4, 0.4, 0.0, 0.2]
        sharpe, vol, avg_daily_ret, cum_ret = sim.run(dt_start, dt_end, ls_symbols, alloc)
        self.assertAlmostEqual(sharpe, 1.028, 3)
        self.assertAlmostEqual(vol, 0.01014, 5)
        self.assertAlmostEqual(avg_daily_ret, 0.000657)
        self.assertAlmostEqual(cum_ret, 1.16487, 5)
