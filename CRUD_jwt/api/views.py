"""System module."""
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .permissions import ProjectPermission
from .serializers import UserSerializer


class indexAPI(APIView):
    """information on the first page for users"""
    def get(self, request):
        """output of reference information"""
        info1 = "Получить токен, после передачи username и password"
        info2 = "Просмотр всех пользователей"
        info3 = "Просмотр пользователя. " \
               "Изменение и удаление доступны для самого пользователя и админа"
        info4 = "проверка токенов 'access'"
        info5 = "отпавление 'refresh' токена для обновления токена 'access'"
        info6 = "сессионная авторизация"
        info7 = "прерываение сессии"
        return Response({"/api-token-auth/": info1, "/api/v1/users/": info2,
                         "/api/v1/users/{id}/": info3, "/api/v1/token/refresh/": info5,
                         "/api/v1/token/verify/": info4, "/api/v1/session/login": info6,
                         "/api/v1/session/logout": info7})


class UserPagination(PageNumberPagination):
    """Pagination for users"""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class UserAPIlist(generics.ListCreateAPIView):
    """Demonstration all users list"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = UserPagination


class UserAPIrud(generics.RetrieveUpdateDestroyAPIView):
    """get put path delete methods"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProjectPermission, )
