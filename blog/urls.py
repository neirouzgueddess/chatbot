from django.urls import path
from . import views  


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article, name='article'),  # Corrected to match the view
    path('getResponse', views.getResponse, name='getResponse'),
    path('blog/getResponse', views.get_response, name='get_response'),

]
