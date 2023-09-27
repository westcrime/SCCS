from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse

from insurance.views import *


class TestUrls(SimpleTestCase):

    def test_cats_url_is_resolved(self):
        url = reverse('home')
        logging.debug(f"test 1 - {resolve(url).func.view_class}")
        self.assertEquals(resolve(url).func.view_class, InsuranceCategories)

    def test_objects_url_is_resolved(self):
        url = reverse('objects')
        logging.debug(f"test 2 - {resolve(url).func.view_class}")
        self.assertEquals(resolve(url).func.view_class, ObjectsOfInsurance)


class TestViews(TestCase):

    def test_login_GET(self):
        client = Client()

        response = client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'insurance/login.html')

    def test_list_agents_GET(self):
        client = Client()

        response = client.get(reverse('list_agents'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'insurance/insurance_agents.html')

    def test_register_GET(self):
        client = Client()

        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'insurance/register.html')

    def test_make_contract_GET(self):
        client = Client()

        response = client.get(reverse('make_contract'))
        self.assertEquals(response.status_code, 302)

    def test_branches_GET(self):
        client = Client()

        response = client.get(reverse('insurance_branches'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'insurance/insurance_branches.html')

    def test_DELETE_deletes_object(self):
        user = User.objects.create(phone_number='+375293068221',
                                   username='username',
                                   password='1234')
        category = InsuranceCategory.objects.create(name='Имущество',
                                                   content='content',
                                                   ins_coef=0.05,
                                                   slug='imushestvo')
        ObjectOfInsurance.objects.create(name="IPhone",
                                         insured_risks='Нормальные',
                                         ins_cat=category,
                                         cost=1000,
                                         user=user)
        response = self.client.get('/delete_object?id=1', {}, True)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(ObjectOfInsurance.objects.all()), 0)
