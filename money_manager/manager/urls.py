from django.urls import path
from .views import transactionListView, create_transaction

urlpatterns = [
    path('all/', transactionListView),
    #path('create/', CreateTransactionView.as_view()),
    path('create/', create_transaction),
]
