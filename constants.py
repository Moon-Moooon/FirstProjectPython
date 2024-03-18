BASE_URL_API: str = "https://www.zulutrade.com/zulutrade-client/trading/api"

STATUS_CODE_GOOD = 200

PARAMETER_TIME_FRAME = {"timeframe": 10000}
PARAMETER_SIZE = {"size": 100}
PARAMETER_PAGE = {"page": 0}
PARAMETER_SORT = {"sort": "dateClosed,desc"}

COLUMNS_NAME = ["currency", "tradeType", "transactionCurrency", "dateOpen", "dateClosed", "lots", "priceOpen",
                "priceClosed", "maxProfit", "worstDrawdown", "interest", "netPnl", "pips", "totalAccumulatedPnl",
                "totalAccumulatedPips"]

COLUMNS_NAME_DATE_TIME = ["dateOpen", "dateClosed"]

FALE_NAME: str = "Pars_Information.csv"