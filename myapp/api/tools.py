# myapp/api/tools.py
from tastytools.api import Api
from tastytools.test.resources import ResourceTestData
from myapp.api.resources import EntryResource, UserResource
from django.contrib.auth.models import User


class EntryTestData(ResourceTestData):
    resource = "entry"

    def get_data(self, data):
        data.set('user', resource='user')
        data.set('pub_date', '2010-12-24T06:23:48')
        data.set('title', 'Lorem ipsum')
        data.set('slug', 'lorem')
        data.set('body', 'Lorem ipsum ad his scripta blandit partiendo...')
        return data

class UserTestData(ResourceTestData):
    resource = "user"

    def get_data(self, data):

        data.set('username', 'foo%d' % User.objects.all().count())
        data.set('email', 'bar@foo.com')
        return data

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(UserResource())

# register our test data
v1_api.register_testdata(EntryTestData)
v1_api.register_testdata(UserTestData)
