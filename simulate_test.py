import unittest
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

    def test_get_stocks_dataframe(self):
        ls_symbols = ["AAPL", "GOOG"]
        df = sim.get_stocks_dataframe("2006/01/01", "2006/01/05", ls_symbols)
        print df
        self.assertTrue(false)

    def test_run(self):
        symbols = ['AAPL']
