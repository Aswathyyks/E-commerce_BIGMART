from django.urls import path
from AdminApp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('add_category/', views.add_category, name="add_category"),
    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:cat_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_ID>/', views.update_category, name="update_category"),
    path('delete_category/<int:del_cat_ID>/', views.delete_category, name="delete_category"),
    path('add_product/', views.add_product, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('edit_product/<int:pro_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:pro_ID>/', views.update_product, name="update_product"),
    path('delete_product/<int:del_pro_ID>/', views.delete_product, name="delete_product"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('contact_display/',views.contact_display,name="contact_display"),
    path('contact_delete/<int:del_contact_ID>/',views.contact_delete,name="contact_delete"),
    path('user_display/', views.user_display, name="user_display"),
    path('user_delete/<int:del_user_ID>/', views.user_delete, name="user_delete"),
    path('order_display/', views.order_display, name="order_display"),
    path('order_delete/<int:del_order>/', views.order_delete, name="order_delete"),
    path('cart_display/', views.cart_display, name="cart_display"),


]