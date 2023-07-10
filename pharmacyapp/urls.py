from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
     path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = 'login'),
     path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('medicine/', views.medicine, name='medicine'),
    path('index/<int:product_id>', views.product_detail, name = 'product_detail'),
    path('sales/', views.sales, name='sales'),
    path('receipts/', views.receipts, name='receipts'),
    path('sell_item/<pk>', views.sell_item, name='sell_item'),
    path('add_to_stock/<pk>', views.add_to_stock, name='add_to_stock'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('receipts/<receipts_id>', views.final_receipt, name ='final_receipt'), 
]   