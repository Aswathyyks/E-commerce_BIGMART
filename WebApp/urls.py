from django.urls import path
from WebApp import views
urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('our_product/',views.our_product,name="our_product"),
    path('filtered_product/<category_name>/', views.filtered_product, name="filtered_product"),
    path('single_product/<int:pro_id>', views.single_product, name="single_product"),
    path('',views.user_register,name="user_register"),
    path('save_user_register/', views.save_user_register, name="save_user_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('cart/', views.cart, name="cart"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('delete_cart/<int:del_ID>/', views.delete_cart, name="delete_cart"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('payment_page/', views.payment_page, name="payment_page"),

]