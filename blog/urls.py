from django.urls import path
from. import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('post/<slug:url>/',views.post1, name ='post'),
    path('category/<slug:url>/', views.category, name = 'category')
]

