from django.urls import path
from .views import blog, blog_single

urlpatterns = [
    path('', blog , name = 'blog'),
    path('<int:id>/', blog_single, name = "blog_single")
]