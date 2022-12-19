from django.urls import path
from .views import HelloAuthView,UserCreateView


urlpatterns = [
    path('', HelloAuthView.as_view(), name='hello'),
    path('signup/', UserCreateView.as_view(), name='new_user'),

]
