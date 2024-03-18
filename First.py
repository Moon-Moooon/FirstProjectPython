import ContentTradingHistory
from WriteDateFile import SaveInfo


def main():
    a = ContentTradingHistory.TradingHistory().get_content()
    SaveInfo.write(a)
    pass

if __name__ == '__main__':
    main()
