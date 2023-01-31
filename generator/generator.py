from automation_VERUM.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name = faker_ru.password()
    )