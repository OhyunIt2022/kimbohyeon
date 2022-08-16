from django.urls import path
from blogapp import views
app_name = 'blogapp'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('<int:pk>/',views.PostDetailView.as_view(), name='detail')

]