import random
import string

class CommonTestData:

    city = "Тула"
    country = "Российская Федерация"
    diplomaId = "123077"
    email = f"{''.join(random.choice(string.ascii_lowercase) for _ in range(10))}@gmail.com"
    finishDate = "2023"
    firstName = "Тест"
    lastName = "Тестовой"
    middleName = "Тестович"
    region = "Тульская область"
    role = "4"
    testResult = "false"
    university = "Алтайский гос. мед. университет"

    def get_payload_registration(self, email):
        data = {
            "city": self.city,
            "country": self.country,
            "diplomaId": self.diplomaId,
            "email": email,
            "finishDate": self.finishDate,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "middleName": self.middleName,
            "region": self.region,
            "role": self.role,
            "testResult": self.testResult,
            "university": self.university
        }
        return data
