from src.api.base_api import BaseApi
from src.test_data.common_test_data import CommonTestData
from src.api.registartion import RegistrationApi


class TestApiRegistration:

    def test_api_registration(self):
        email = RegistrationApi().registration_email()
        data = CommonTestData().get_payload_registration(email=email)
        resp = BaseApi().post_application(endpoint='front/auth/completeRegistration', payload=data)
        assert resp.get('token')
