# Backtrader

Feel free to choose your own symbol freqency and period

Be aware that not all freqencies and periods have data

```text
usage: sma.py [-h] [--symbol SYMBOL] [--start START] [--end END] [--freq FREQ] [--l_period L_PERIOD] [--s_period S_PERIOD]

Simple Moving Average Stratergy

optional arguments:
  -h, --help           show this help message and exit
  --symbol SYMBOL      Yahoo symbol (default: BTC)
  --start START        Ending date in YYYY-MM-DD format (default: 2022-01-01)
  --end END            Ending date in YYYY-MM-DD format (default: 2023-02-22)
  --freq FREQ          [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo] (default: 1d)
  --l_period L_PERIOD  Long period for MA (default: 30)
  --s_period S_PERIOD  short period for MA (default: 10)
```

