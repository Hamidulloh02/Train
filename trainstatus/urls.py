from django.urls import path, reverse_lazy, re_path
from .views import WorkStatus,WorkStatusAdd,WorkStatusDelete, YulakListView, StanssiyaView, YulakAdd, YulakEditView


urlpatterns = [
    path('accounts/profile/', WorkStatus.as_view(), name='home'),
    path('add/', WorkStatusAdd.as_view(), name='home'),
    path('del/<int:pk>/', WorkStatusDelete.as_view(), name='home'),
    path('yul/', YulakListView.as_view(), name='yulak'),
    path('yul/del/<int:pk>/', YulakEditView.as_view(), name='home'),
    path('region/', StanssiyaView.as_view(), name='region'),
    path('yul/add/', YulakAdd.as_view(), name='add_yul'),


]