import backtrader as bt

class Nothing(bt.SignalStrategy):
    def __init__(self):
        pass

    def next(self):
        pass

    def notify_order(self, order):
        pass