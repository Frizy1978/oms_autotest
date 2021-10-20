class JSONFixture:

    @staticmethod
    def for_create_order_tobacco(expectedStartDate, factoryId, poNumber, gtin, quantity, serialNumberType, serialNumbers, templateId):
        json = {
            "expectedStartDate": expectedStartDate,
            "factoryAddress": "ul. First Tobacco productions h.23",
            "factoryCountry": "RU",
            "factoryId": factoryId,
            "factoryName": "Lednyoff Gold Tobacco Factory",
            "poNumber": poNumber,
            "productCode": "ABCD123456",
            "productDescription": "Free Cigarettes",
            "productionLineId": "111-222",
            "products": [
                {
                    "gtin": gtin,
                    "mrp": 1000,
                    "quantity": quantity,
                    "serialNumberType": serialNumberType,
                    "serialNumbers": serialNumbers,
                    "templateId": templateId
                }]
            }
        return json

    @staticmethod
    def for_utilization_report_tobacco(sntins, usageType, productionDate):
        json = {
          "sntins":sntins,
          "usageType" : usageType,
          "productionLineId" : "1-11-222",
          "productionOrderId":"Best&bad tabacco",
          "productionDate": productionDate,
          "brandcode" : "Lednyoff Gold Tobacco"
        }
        return json


