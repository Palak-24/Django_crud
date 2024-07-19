from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LoginAPIView,ProfileViewSet
from .views import RegisterView,UserListView

router=DefaultRouter()
router.register(r'profiles',ProfileViewSet)
urlpatterns=[
    path('login/',LoginAPIView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('users/', UserListView.as_view(), name='userlist'),

    path('',include(router.urls)),
]