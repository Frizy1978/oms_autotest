import pytest
import json
from requests import Response
from tests.utils.api import Api

class TestOrderOms:

    @staticmethod
    def setup():
        assert 1 == 1

    @staticmethod
    def teardown():
        assert 1 == 1

    @pytest.mark.api
    def test_ping_oms(self):
        result: Response = Api.ping()
        #response_json = result.json()

        assert 200 == result.status_code
       # assert Api.OMS_ID == response_json['omsId']