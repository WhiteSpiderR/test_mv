from src.api.base_api import BaseApi
from src.test_data.common_test_data import CommonTestData


class RegistrationApi:

    def registration_email(self):
        email = CommonTestData.email
        data = {"email": email,
                "roleId": CommonTestData.role,
                "url": "patient"}
        BaseApi().post_application(endpoint='front/auth/continueRegistration', payload=data)
        return email

