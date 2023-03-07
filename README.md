# Backtrader

An application to run backtesting using Backtrader



## Environment and Installation

```
conda create --name bt python=3.8
conda activate bt

conda install pandas 
pip install backtrader
pip install yfinance

pip install matplotlib==3.2.2
```



## Config Files

You can adjust everything in the codeby making changes to `config.json`.

```json
{
    "data_args":{
        "symbol": "AAPL",
        "fromdate": "2020-01-01",
        "todate": "2023-02-22",
        "freq": "1d",
        "read_from_csv": null
    },
    "strategy_args":{
        "strategy_path": "strategy.sma",
        "strategy_class": "SmaCross",
        "parameters":{
            "l_period": 30,
            "s_period": 10
        }
    },
    "commission_args":{
        "commission": 0.01,
        "margin": null,
        "mult": 1.0
    },
    "broker_args":{
        "cash":1000000,
        "slippage": 0
    }
}
```

Config files has 4 sections

-  `data_args`: arguments for data, either specify your data prefered and extract from online database, or prepare your own data and put the path in `read_from_csv`. Note that if your are using your own data, all the other parameters is ignored, the data has to match the Yahoo format.
- `strategy_args`: arguments for stategies, chose the path and class of your implemented strategy, pass whatever customized parameter through `parameters` .
- `commission_args`: arguments to control the commission schemes.
- `broker_args`: arguments to customize broker behaviors.

## Strategy



## Commission 

- `commission` (default: `0.0`)

  Monetary units in absolute or percentage terms each action costs.

  In the above example it is 2.0 euros per contract for a `buy` and again 2.0 euros per contract for a `sell`.

  The important issue here is when to use absolute or percentage values.

  - If `margin` evaluates to `False` (it is False, 0 or None for example) then it will be considered that `commission` expresses a percentage of the `price` times `size` operatin value
  - If `margin` is something else, it is considered the operations are happenning on a `futures` like intstrument and `commission` is a fixed price per `size` contracts

- `margin` (default: `None`)

  Margin money needed when operating with `futures` like instruments. As expressed above

  - If a no `margin` is set, the `commission` will be understood to be indicated in percentage and applied to `price * size` components of a `buy` or `sell` operation
  - If a `margin` is set, the `commission` will be understood to be a fixed value which is multiplied by the `size` component of `buy` or `sell` operation

- `mult` (default: 1.0)

  For `future` like instruments this determines the multiplicator to apply to profit and loss calculations.

  This is what makes futures attractive and risky at the same time.

## Broker

