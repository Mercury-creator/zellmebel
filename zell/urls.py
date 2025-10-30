from django.urls import path

from . import views

app_name = "zell"
urlpatterns = [
    path("", views.main, name="main"),
    path("products/", views.products, name="products"),
    path("<int:pk>/", views.main_detail, name="main_detail"),
    path("<int:category_id>/<int:product_id>/", views.product_detail, name="product_detail"),
    path("about_us/", views.about_us, name="about_us"),
    path("contacts/", views.contacts, name="contacts"),
    path("<str:page", views.other_page, name="other_page")
]