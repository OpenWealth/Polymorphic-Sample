# coding: utf-8

from fastapi.testclient import TestClient


from API.models.financial_instrument import FinancialInstrument  # noqa: F401


def test_get_instrument_by_id(client: TestClient):
    """Test case for get_instrument_by_id

    This is a summary
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/financial-instruments/{instrumentId}".format(instrumentId='instrument_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

