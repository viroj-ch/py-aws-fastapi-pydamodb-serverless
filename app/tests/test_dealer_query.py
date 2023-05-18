from moto import mock_dynamodb
from pynamodb.connection import Connection

from app.shared.models import dealer

conn = Connection(region='ap-southeast-1')


@mock_dynamodb
def test_dealer():
    # given
    dealer.DealerModel.create_table()

    # item = dealer.DealerModel.from_raw_data({
    #     "dealerCode": {
    #         "S": "43081"
    #     },
    #     "createdDate": {
    #         "S": "2023-03-16T11:34:17.724+07:00"
    #     },
    #     "dealerNameThai": {
    #         "S": "นายฉรายุทธ ประกอบสุข"
    #     },
    #     "dealerStatus": {
    #         "S": "S"
    #     },
    #     "modifiedDate": {
    #         "S": "2023-05-17T12:34:44.020+07:00"
    #     },
    #     "priorityId": {
    #         "S": "BLANK"
    #     },
    #     "priorityLevel": {
    #         "N": "0"
    #     },
    #     "taxId": {
    #         "S": "3210500225811"
    #     }
    # })
    # item.save()
    item = dealer.DealerModel(
        dealerCode="43081",
        createdDate="2023-03-16T11:34:17.724+07:00",
        dealerNameThai="นายฉรายุทธ ประกอบสุข",
        dealerStatus="S",
        modifiedDate="2023-05-17T12:34:44.020+07:00",
        priorityId="BLANK",
        priorityLevel=0,
        taxId="3210500225811"
    )
    item.save()

    # when
    result = dealer.DealerModel.get('43081')

    # then
    assert result.priorityId == item.priorityId
    assert result.dealerCode == item.dealerCode
    assert result.attribute_values == item.attribute_values
