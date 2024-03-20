from django.urls import path

from .views import create_bank, bank_info, index

app_name = 'bank'

urlpatterns = [
    path("bank/<int:bank_id>", bank_info, name='bank_info'),
    path("bank/index", index, name='index'),
    path("create_bank/", create_bank, name='create_bank'),
    # path("create_accountant/", create_accountant, name='create_accountant'),
    # path("accountant/", accountant, name='accounts'),
]
