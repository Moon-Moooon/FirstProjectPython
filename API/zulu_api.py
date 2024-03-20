from http import HTTPStatus

from ZULU import constants
from ZULU.API.base_api import BaseApi
from ZULU.our_logger import OurLogger
from ZULU.utils.helpers import Helpers


class ZuluApi:
    _TRADES_HISTORY_ENDPOINT = "/trades/history"
    logg = OurLogger().get_logger(__name__)

    @staticmethod
    def get_request(url, params=None):
        request = BaseApi.get_request(url, params)
        return request

    @staticmethod
    def get_json_request(request):
        return Helpers.get_json_request(request)

    @staticmethod
    def get_request_trading_history(*, parameter_page, provider_id):
        _parameter_provider_id = "/providers/" + str(provider_id)
        url_end_point = constants.BASE_URL_API + _parameter_provider_id + ZuluApi._TRADES_HISTORY_ENDPOINT
        params = {"item_one": constants.PARAMETER_TIME_FRAME, "item_two": parameter_page,
                  "item_three": constants.PARAMETER_SIZE, "item_four": constants.PARAMETER_SORT}
        return ZuluApi.get_request(url_end_point, params)

    @staticmethod
    def check_status_code(request):
        if request.status_code != HTTPStatus.OK:
            ZuluApi.logg.critical(f"{request.status_code} is not good")
            raise Exception(f"{request.status_code} is not good")

    @staticmethod
    def request_to_json(request):
        try:
            return ZuluApi.get_json_request(request)
        except:
            ZuluApi.logg.critical(f"request cant be json: {request}")
            pass

    @staticmethod
    def check_json_on_impotent_name(*, json_file, list_name):
        for line in list_name:
            if json_file[line] is None:
                ZuluApi.logg.critical(f"{line} is not exist, in JsonFile")
                raise Exception(f"{line} is not exist, in JsonFile")
