from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.

class ArticleCreateTest(APITestCase):
    def setUp(self):
        self.user_data = {'username':'john', 'passwrod':'johnpassword'} 
        self.article_data = {'title':'some title', 'content':'some content'}
        self.user = User.objects.create_user('john', 'johnpassword')
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access'] 
        
    
    
    def test_fail_if_not_logged_in(self):
        url = reverse('article_view')
        response = self.client.post(url, self.article_data)
        self.assertEqual(response.status_code, 401)