from django.urls import path
from .views import transaction_list_view, create_transaction


urlpatterns = [
    path('all/', transaction_list_view),
    path('create/', create_transaction),
]
