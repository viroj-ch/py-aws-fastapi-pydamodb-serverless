import pytest
from fastapi.testclient import TestClient
from moto import mock_dynamodb
from pynamodb.connection import Connection

from app.main import app
from app.shared.models import dealer

conn = Connection(region='ap-southeast-1')
client = TestClient(app)


def test_search():
    # given
    query_param = 'x'

    # when
    response = client.get(f"/search?query={query_param}")

    # then
    assert response.status_code == 200
    assert response.json() == {'message': f'You searched for {query_param}'}


class TestGetDealerByDealerCode:
    @mock_dynamodb
    def test_get_dealer_by_dealer_code_given_item_exist(self):
        # given
        dealer.DealerModel.create_table()
        dealer_code = '43081'

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
        response = client.get(f"/dealer/{dealer_code}")

        # then
        assert response.status_code == 200
        assert response.json() == {
            "dealerCode": "43081",
            "createdDate": "2023-03-16T11:34:17.724+07:00",
            "dealerNameThai": "นายฉรายุทธ ประกอบสุข",
            "dealerStatus": "S",
            "modifiedDate": "2023-05-17T12:34:44.020+07:00",
            "priorityId": "BLANK",
            "priorityLevel": 0,
            "taxId": "3210500225811"
        }

    @mock_dynamodb
    def test_get_dealer_by_dealer_code_given_item_not_exist(self):
        # given
        dealer.DealerModel.create_table()

        # when
        response = client.get("/dealer/43081")

        # then
        assert response.status_code == 404
        assert response.json() == {'detail': 'Item not found'}


class TestGetDealer:
    @mock_dynamodb
    def test_get_dealer_by_status_and_priority_id_given_item_exists(self):
        # given
        # when
        # then
        pass

    @pytest.mark.parametrize("query_params", [
        pytest.param('', id="given blank"),
        pytest.param('?priority_id=BLANK', id="missing status"),
    ])
    def test_get_dealer_by_status_and_priority_id_given_missing_required_field(self, query_params):
        # given
        # when
        response = client.get(f"/dealer{query_params}")

        # then
        assert response.status_code == 422
        assert response.json() == {'detail': [{'loc': ['query', 'dealer_status'],
                                               'msg': 'field required',
                                               'type': 'value_error.missing'}]}
