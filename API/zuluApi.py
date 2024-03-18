from API.baseApi import BaseApi
import constants


class ZuluApi:
    @staticmethod
    def get_reqest(url, paarams=None):
        request = BaseApi.get_request(url, paarams)
        return request

    @staticmethod
    def get_json_request(request):
        return BaseApi.get_json_request(request)

    @staticmethod
    def get_reqest_traiding_histori(parameter_page):
        second_fragment_url = '/providers/420820/trades/history'
        url_end_point = constants.BASE_URL_API + second_fragment_url
        pool_params = [constants.PARAMETER_TIME_FRAME, parameter_page, constants.PARAMETER_SIZE,
                       constants.PARAMETER_SORT]
        params = {K: V for i in pool_params for K, V in i.items()}
        return ZuluApi.get_reqest(url_end_point, params)

    @staticmethod
    def check_status_code(request):
        if request.status_code != constants.STATUS_CODE_GOOD:
            raise Exception(f"{request.status_code} is not good")

    @staticmethod
    def request_to_json(request):
        try:
            return ZuluApi.get_json_request(request)
        except:
            raise Exception(f"{request} Can't be converted to json")

    @staticmethod
    def check_json_on_impotent_name(*, json_file, list_name):
        for line in list_name:
            if json_file[line] is None:
                raise Exception(f"{line} is not exist, in JsonFile")
