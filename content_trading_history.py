from ZULU.constants import (COLUMNS_NAME, COLUMNS_NAME_DATE_TIME,
                            PARAMETER_PAGE)

from utils.convert_time_date import ConvertTimeDate
from ZULU.API import ZuluApi


class TradingHistory:
    def __init__(self, provider_id):
        self.__page = PARAMETER_PAGE
        self.__IsNext = True
        self.__response_json: dict = {}
        self.__contentPack = []
        self.__provider_id = provider_id

    def get_content(self):
        while self.__IsNext:
            self.__craft_content()
            self.__page += 1
            self.__check_on_last()
        return self.__contentPack

    def __check_on_last(self):
        last_bool = self.__response_json["last"]
        if last_bool:
            self.__IsNext = False

    def __craft_content(self):
        self.__response_json = TradingHistory.get_json_trading_history(self.__page, self.__provider_id)
        content = self.__response_json["content"]
        for item in content:
            _reset_content = self.__get_content_from_page(item)
            self.__contentPack.append(_reset_content)

    def __get_content_from_page(self, item):
        _reset_content = {}
        for column_name in COLUMNS_NAME:
            _reset_content[column_name] = item[column_name]
            if column_name in COLUMNS_NAME_DATE_TIME:
                _reset_content[column_name] = ConvertTimeDate().convert(_reset_content[column_name])
        return _reset_content

    @staticmethod
    def get_json_trading_history(parameter_page, provider_id):
        output = ZuluApi.get_request_trading_history(parameter_page=parameter_page, provider_id=provider_id)
        ZuluApi.check_status_code(output)
        json_file = ZuluApi.request_to_json(output)
        important_name = ["content", "last"]
        ZuluApi.check_json_on_impotent_name(json_file=json_file, list_name=important_name)
        return json_file
