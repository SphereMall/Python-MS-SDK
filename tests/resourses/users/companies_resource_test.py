from ms_sdk.Entities.Company import Company
from tests.settings import setup_client


class TestCompaniesResource:

    def test_service_get_list(self):
        companies = setup_client().companies().all()

        try:
            assert companies[0]
            for company in companies:
                isinstance(type(company), Company)
        except:
            isinstance(type(companies), Company)