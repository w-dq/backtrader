from datetime import datetime
import argparse


import backtrader as bt
from pandas_datareader import data as pdr
import yfinance as yf
import yfinance.shared as shared

class SmaCross(bt.SignalStrategy): 
    params = (('long_p', None),('short_p', None))
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.params.short_p), bt.ind.SMA(period=self.params.long_p)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

def prep_offline_data(symbol, fromdate, todate, freq):
    data =  bt.feeds.PandasData(dataname=yf.download(symbol, fromdate, todate, interval = freq))
    fails = list(shared._ERRORS.keys())
    if fails:
        raise RuntimeError("\n [Custom Error Msg] Fail to download %s symbol" % ("|".join(fails)))
    return data

def run(data_feed,long_p,short_p):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaCross,long_p=long_p,short_p=short_p)
    cerebro.adddata(data_feed)
    cerebro.run()
    cerebro.plot()
    
def parse_args(pargs=None):

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Simple Moving Average Stratergy')

    parser.add_argument('--symbol',required=False, default='BTC',
                        help='Yahoo symbol')

    parser.add_argument('--start', required=False, default="2022-01-01",
                        help='Ending date in YYYY-MM-DD format')

    parser.add_argument('--end', required=False, default="2023-02-22",
                        help='Ending date in YYYY-MM-DD format')

    parser.add_argument('--freq', required=False, default='1d',
                        help=('[1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]'))
    
    parser.add_argument('--l_period', required=False, default=30, type=int,
                        help=('Long period for MA'))

    parser.add_argument('--s_period', required=False, default=10, type=int,
                        help=('short period for MA'))           

    return parser.parse_args(pargs)



if __name__ == "__main__":
    args = parse_args()
    data_feed = prep_offline_data(args.symbol, args.start, args.end, args.freq)
    run(data_feed, args.l_period, args.s_period)