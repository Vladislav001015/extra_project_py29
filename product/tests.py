from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from product.views import CategoryModelViewSet, ProductModelViewSet
from product.models import Category, Product
from account.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView


class CategoryTest(APITestCase):
    """
        Тесты на модель категорий
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user('test@test.com', '1', is_active=True)
        
    def test_get_category(self):
        request = self.factory.get('api/v1/product/category')
        view = CategoryModelViewSet.as_view({'get': 'list'})
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 0
        
    def test_post_category(self):
        data = {
            'name': 'Test'
        }
        request = self.factory.post('api/v1/product/category', data)
        force_authenticate(request, self.user)
        view = CategoryModelViewSet.as_view({'post': 'create'})
        response = view(request)
        
        assert response.status_code == 201
        assert Category.objects.count() == 1


class ProductTest(APITestCase):
    """
        Тесты на модель продуктов
    """
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user('test@test.com', '1', is_active=True)
        self.set_up_category()
        self.access_token = self.set_up_token()
    
    def set_up_token(self):
        data = {
            'email': 'test@test.com',
            'password': '1'
        }
        request = self.factory.post('api/v1/account/login/', data)
        view = TokenObtainPairView.as_view()
        response = view(request)
        return response.data.get('access')
    
    @staticmethod
    def set_up_category():
        Category.objects.create(name='test')

    def test_get_prodoct(self):
        request = self.factory.get('api/v1/product/', HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        # force_authenticate(request, self.user)
        view = ProductModelViewSet.as_view({'get': 'list'})
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 0
    
    def test_post_product(self):
        image = open('media/images/Снимок_экрана_2023-09-18_в_18.09.37.png', 'rb')
        data = {
            'owner': self.user.id,
            'category': Category.objects.first().name,
             'title': 'test product',
             'price': 100,
             'image': image
        }
        request = self.factory.post('api/v1/product/', data=data, HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        image.close()
        view = ProductModelViewSet.as_view({'post': 'create'})
        response = view(request)
        assert response.status_code == 201
        assert response.data.get('title') == 'test product'
        assert Product.objects.count() == 1
        