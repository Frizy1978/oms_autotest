import configparser
import logging
import json
import urllib.parse

from allure_commons._allure import step
from tests.utils.http_manager import HttpManager
from tests.utils.json_fixture import JSONFixture

class Api:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    configFilePath = 'C:\\Users\\d.lednev\\PycharmProjects\\oms_autotest\\simple_config.ini'
    parser.read(configFilePath)

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'clientToken':'7a2fd0d1-5c0c-460a-b12f-52ae4993bcac'}

    @staticmethod
    def make_url(url, *res, **params):
        urls = url
        for r in res:
            urls = '{}/{}'.format(urls, r)
        if params:
            urls = '{}?{}'.format(urls, urllib.parse.urlencode(params))
        return urls

    BASE_URL = parser.get('oms', 'url')
    PRODUCT_GROUP = parser.get('oms', 'productGroup')
    OMS_ID = parser.get('oms', 'omsId')

    PING = make_url(BASE_URL,'tobacco','ping', omsId=OMS_ID)

    # CREATE_ORDER = BASE_URL + "orders"
    # CHECK_ORDER_STATUS = BASE_URL + "/buffer/status"
    # GET_CODES = BASE_URL + "codes"
    # SEND_REPORT_UTILIZATION = BASE_URL + "utilisation"
    # GET_REPORT_STATUS = BASE_URL + "report/info"
    # SENT_REPORT_DROPOUT = BASE_URL + "dropout"
    # SENT_REPORT_AGGREGATION = BASE_URL + ""

    @staticmethod
    def ping():
        with step("Ping"):
            url = Api.PING
            print('url =>{}'.format(url))
            result = HttpManager.ping(url)
            Api.LOGGER.info('TEST 1: ping for user omsId:{} with token:'.format(Api.OMS_ID))
            assert 200 == result.status_code
            assert result.json()['omsId'] == Api.OMS_ID



