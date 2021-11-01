from unittest import mock
from apis.dataprovider import dataprovider
from tests import fixtures


@mock.patch("apis.dataprovider.dataprovider.get_data")
def test__model_get_data_success(
    mock_model_get_data: mock.Mock,
):
    MOCK_DATA = fixtures.data_entity()
    mock_model_get_data.return_value = MOCK_DATA
    response =  dataprovider.get_data()
    assert response == MOCK_DATA