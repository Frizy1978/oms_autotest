import requests


class HttpManager:

    @staticmethod
    def ping(url):
        result = requests.get(url, headers={'clientToken':'7a2fd0d1-5c0c-460a-b12f-52ae4993bcac'})
        return result

    @staticmethod
    def create_order():
        pass

    @staticmethod
    def get_order_status():
        pass

    @staticmethod
    def get_codes_from_order():
        pass

    @staticmethod
    def sent_report_utilization():
        pass

    @staticmethod
    def check_report_status():
        pass


