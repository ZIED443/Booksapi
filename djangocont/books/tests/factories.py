import factory
from faker import Factory as FakerFactory
from ..models import  User, Auhor, Book, Bookreservation

faker = FakerFactory.create()



class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda _: faker.email())
    user_name = factory.LazyAttribute(lambda _: faker.user_name())
    password = factory.PostGenerationMethodCall('set_password', 'password')  
    is_staff = False
    is_active = True
    sex = 'male'

class AuhorFactory(factory.Factory):
    class Meta:
        model = Auhor

    name = factory.LazyAttribute(lambda _: faker.name())
    birthday = faker.date_time_this_decade()

class BookFactory(factory.Factory):
    class Meta:
        model = Book

    author = factory.SubFactory(AuhorFactory)
    date_release = faker.date_time_this_decade()
    name = factory.LazyAttribute(lambda _: faker.sentence())

class BookreservationFactory(factory.Factory):
    class Meta:
        model = Bookreservation

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
    date1 = faker.date_time_this_decade()
    date2 = faker.date_time_this_decade()
