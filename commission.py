# import backtrader as bt

# class CommissionScheme(bt.CommInfoBase):
#     params = (
#         ("my_param", 0.01),  # Example custom parameter
#     )

#     def getsize(self, price, cash):
#         # Implement your custom size calculation here...
#         return size

#     def getcommission(self, size, price, **kwargs):
#         # Implement your custom commission calculation here...
#         return commission

#     def getmargin(self, size, price, **kwargs):
#         # Implement your custom margin calculation here...
#         return margin


# cerebro.broker.addcommissioninfo(MyCommissionScheme(my_param=0.05))
