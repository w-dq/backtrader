import importlib
import json
import types

import pandas as pd
import yfinance as yf
import yfinance.shared as shared
import backtrader as bt

from broker import MyBroker

import matplotlib.pyplot as plt

# Analyzers
# SharpeRatio: SQN: DrawDown: TimeReturn: VWR: TradeAnalyzer: PyFolio: AnnualReturn: Calmar: Omega: Sortino: TailRisk: 

def prep_data_feed(symbol, fromdate, todate, freq, read_from_csv):
    if read_from_csv: 
        df = pd.read_csv(read_from_csv, index_col='Date', parse_dates=True)
        data = bt.feeds.PandasData(dataname = df)
    else:
        data =  bt.feeds.PandasData(dataname=yf.download(symbol, fromdate, todate, interval = freq))
        fails = list(shared._ERRORS.keys())
        if fails:
            raise RuntimeError("\n [Custom Error Msg] Fail to download %s symbol" % ("|".join(fails)))
    return data

def run(data_feed,strategy_class,broker_info,commission_info,strategy_args):
    cerebro = bt.Cerebro()

    cerebro.addstrategy(strategy_class,args=strategy_args)

    cerebro.adddata(data_feed)

    my_broker = MyBroker(args=broker_info)
    cerebro.setbroker(my_broker)

    cerebro.broker.setcommission(commission = commission_info.commission, margin = commission_info.margin,mult = commission_info.mult)

    # analyzer = bt.analyzers.SharpeRatio
    # cerebro.addanalyzer(analyzer)

    results = cerebro.run()

    return results

def load_config():
    strategy_args = types.SimpleNamespace()
    commission_args = types.SimpleNamespace()
    broker_args = types.SimpleNamespace()

    with open('config.json', 'r') as f:
        data = json.load(f)
        for key, value in data["strategy_args"].items():
            setattr(strategy_args, key, value)
        for key, value in data["commission_args"].items():
            setattr(commission_args, key, value)
    return data["data_args"],strategy_args,commission_args,data["broker_args"]

if __name__ == "__main__":
    data_config,strategy_config,commission_config,broker_config = load_config()

    data_feed = prep_data_feed(**data_config)

    module = importlib.import_module(strategy_config.strategy_path)
    Strategy = getattr(module, strategy_config.strategy_class)
    pnl = run(data_feed, Strategy, broker_config, commission_config, strategy_config.parameters)
    print(pnl)