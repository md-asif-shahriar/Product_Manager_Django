from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('api/product-category/', views.getCategory, name="product-category"),

    path('api/product-category/<int:pk>/',
         views.getOneCategory, name="category-details"),

    path('api/product-category/add/', views.addCategory, name="add-category"),

    path('api/product-category/update/<int:pk>/',
         views.updateCategory, name="update-category"),

    path('api/product-category/delete/<int:pk>/',
         views.deleteCategory, name="delete-category"),
]
