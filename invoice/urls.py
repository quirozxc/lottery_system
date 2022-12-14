from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('last/download/', views.export_invoice, name='export_invoice'),
    path('<int:invoice>/resume/download/', views.export_invoice, name='export_invoice'),
    path('<int:invoice>/matrix/download/', views.export_matrix, name='export_matrix'),
    path('user/', views.user_invoice_list, name='user_invoice_list'),
    path('management/', views.management, name='management'),
    path('update-pay/betting-agency/<int:betting_agency>', views.management, name='management'),
    path('pay-to-manager/', views.pay_to_manager, name='pay_to_manager'),
]