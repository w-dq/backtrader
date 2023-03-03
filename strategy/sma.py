import backtrader as bt

class SmaCross(bt.SignalStrategy): 
    params = (('args', None),)
    def __init__(self):
        short_p = self.params.args["s_period"]
        long_p = self.params.args["l_period"]

        sma1, sma2 = bt.ind.SMA(period=short_p), bt.ind.SMA(period=long_p)
        self.crossover = bt.ind.CrossOver(sma1, sma2)
        self.order = None

    def next(self):
        if self.order:  
            self.cancel(self.order)  
    
        if not self.position:  
            if self.crossover > 0:             
                self.order = self.buy()
        elif self.crossover < 0:            
            self.order = self.close()

    def notify_order(self, order):
        pass
        # if order.status in [order.Submitted, order.Accepted]:
        #     return
        # if order.status in [order.Completed, order.Canceled, order.Margin]:
        #     if order.isbuy():
        #         self.log(
        #             'BUY EXECUTED, ref:%.0f，Price: %.4f, Size: %.2f, Cost: %.4f, Comm %.4f' %
        #             (order.ref,
        #              order.executed.price,
        #              order.executed.size,
        #              order.executed.value,
        #              order.executed.comm))
        #     else:
        #         self.log('SELL EXECUTED, ref:%.0f, Price: %.4f, Size: %.2f, Cost: %.4f, Comm %.4f' %
        #                 (order.ref,
        #                 order.executed.price,
        #                  order.executed.size,
        #                 order.executed.value,
        #                 order.executed.comm))
        

