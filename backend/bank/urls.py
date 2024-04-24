from django.urls import path

from .views import create_bank, bank_info, index, create_manager, create_client, create_accountant

app_name = 'bank'

urlpatterns = [
    path("bank/<int:bank_id>/", bank_info, name='bank_info'),
    path("", index, name='index'),
    path("create_bank/", create_bank, name='create_bank'),
    path("create_accountant/", create_accountant, name='create_accountant'),
    # path("accountant/", accountant, name='accounts'),
    path("create_manager/", create_manager, name='create_manager'),
    path("create_client/", create_client, name='create_client'),
]
