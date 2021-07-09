import random
import faker

fake = faker.Faker()
n = 3
def person():
    name = fake.name()
    date = str(fake.date_between(start_date='-50y', end_date='-20y'))
    address = fake.address();
    cpf = random.randint(11111111111, 91111111111)
    return date, name, cpf, address

persons = []
for i in range(n):
    print(person()[2])
