from constants import COLUMNS_NAME
from constants import COLUMNS_NAME_DATE_TIME
from constants import PARAMETER_PAGE

from ConvertTimeDate import ConvertTimeDate

from API import ZuluApi


class TradingHistory:
    def __init__(self):
        self.__page = PARAMETER_PAGE
        self.__IsNext = True
        self.__response_json: dict = {}
        self.__contentPack = []

    @staticmethod
    def get_content():
        obj = TradingHistory()
        while obj.__IsNext:
            obj.__craft_content()
            obj.__page["page"] += 1
            obj.__next()
        return obj.__contentPack

    def __next(self):
        last_bool = self.__response_json["last"]
        if last_bool:
            self.__IsNext = False

    def __craft_content(self):
        self.__response_json = TradingHistory.get_json_file(self.__page)
        content = self.__response_json["content"]
        for item in content:
            _reset_content = {}
            for column_str in COLUMNS_NAME:
                _reset_content[column_str] = item[column_str]
                if column_str in COLUMNS_NAME_DATE_TIME:
                    _reset_content[column_str] = ConvertTimeDate.convert(_reset_content[column_str])
            self.__contentPack.append(_reset_content)

    @staticmethod
    def get_json_file(parameter_page):
        output = ZuluApi.get_reqest_traiding_histori(parameter_page)
        json_file = TradingHistory.check_request(output)
        important_name = ["content", "last"]
        ZuluApi.check_json_on_impotent_name(json_file=json_file, list_name=important_name)
        return json_file

    @staticmethod
    def check_request(request):
        ZuluApi.check_status_code(request)
        json_file = ZuluApi.request_to_json(request)
        return json_file
