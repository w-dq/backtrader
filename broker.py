import backtrader as bt

class MyBroker(bt.brokers.BackBroker):
    params = (
        ("args", None),  # The amount of slippage to simulate (in dollars or percentage)
    )

    def __init__(self):
        super().__init__()
        self._last_prices = {}  # A dictionary to store the last price for each asset
        self.slippage = self.params.args["slippage"]
        self.set_cash(self.params.args["cash"])


    def _simulate_slippage(self, order, price):
        # Calculate the slippage amount
        if self.slippage > 0:
            slippage = self.slippage

            # Adjust the execution price by the slippage amount
            if order.isbuy():
                price += slippage
            else:
                price -= slippage

        return price

    def _get_exec_price(self, data, order):
        # Get the current price for the asset
        price = data.close[0]

        # Simulate slippage by adjusting the execution price
        price = self._simulate_slippage(order, price)

        # Store the last price for the asset
        self._last_prices[data] = price

        return price

    def _get_fill_size(self, data, order):
        # Use the default fill size logic
        fill_size = super()._get_fill_size(data, order)

        # Adjust the fill size based on the remaining cash and the current price
        if order.isbuy():
            price = self._last_prices[data]
            remaining_cash = self.get_cash() - fill_size * price
            fill_size = min(fill_size, remaining_cash // price)
        else:
            fill_size = min(fill_size, self.getposition(data).size)

        return fill_size