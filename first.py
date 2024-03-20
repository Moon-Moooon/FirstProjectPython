from ZULU import content_trading_history
from ZULU.constants import DEFAULT_PROVIDER_ID
from ZULU.our_logger import OurLogger
from ZULU.utils.write_date_file import SaveInfo

def main():
    a = content_trading_history.TradingHistory(DEFAULT_PROVIDER_ID).get_content()
    SaveInfo.write(a)

if __name__ == '__main__':
    main()
