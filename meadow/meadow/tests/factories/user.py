import factory

from meadow.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user #{n}")
    password = factory.Sequence(lambda n: f"password #{n}")

    @classmethod
    def _create(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._create(create, **kwargs)
        if password:
            # dirty hack to get access to a real password in tests
            setattr(user, "real_password", password)
            user.set_password(password)
            if create:
                user.save()
        return user
