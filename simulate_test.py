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

    def test_calc_cum_return(self):
        returns = [.009, -.007, .008]
        cum_return = sim.calc_cum_return(returns)
        self.assertAlmostEqual(cum_return, 0.009952, 6)

    def test_run(self):
        dt_start = dt.datetime(2011, 01, 01)
        dt_end = dt.datetime(2011, 01, 8)
        ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
        alloc = [0.4, 0.4, 0.0, 0.2]
        vol, avg_daily_ret, sharpe, cum_ret = sim.run(dt_start, dt_end, ls_symbols, alloc)
        self.assertAlmostEqual(sharpe, -2.1709, 3)
        self.assertAlmostEqual(vol, 0.00327, 5)
        self.assertAlmostEqual(avg_daily_ret, -0.000448657, 9)
        self.assertAlmostEqual(cum_ret, -0.00226798, 8)
