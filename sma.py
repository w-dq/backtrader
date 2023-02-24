from datetime import datetime
import argparse


import backtrader as bt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

class SmaCross(bt.SignalStrategy): 
    params = (('d0', None),('d1', None))
    def __init__(self):
        print(self.params.d1,self.params.d0)
        sma1, sma2 = bt.ind.SMA(period=self.params.d1), bt.ind.SMA(period=self.params.d0)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

def prep_offline_data(symbol, fromdate, todate, freq,filename):
    data_raw = pdr.get_data_yahoo(symbol, start=fromdate, end=todate, interval=freq)
    data_raw.to_csv(filename)    

def run(filename,long_p,short_p):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaCross,d0=long_p,d1=short_p)
    data_feed = bt.feeds.YahooFinanceCSVData(dataname=filename)
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

    parser.add_argument('--filename', required=False, default='data.csv',
                        help=('name of the file that data is stored in'))
    
    parser.add_argument('--l_period', required=False, default=30, type=int,
                        help=('Long period for MA'))

    parser.add_argument('--s_period', required=False, default=10, type=int,
                        help=('short period for MA'))           

    return parser.parse_args(pargs)



if __name__ == "__main__":
    args = parse_args()
    prep_offline_data(args.symbol,args.start,args.end,args.freq,args.filename)
    print(args.long_period)
    run(args.filename,args.l_period,args.s_period)