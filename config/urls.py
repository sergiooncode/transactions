from django.contrib import admin
from django.urls import path

from transactions.controllers.summary_by_account import SummaryByAccountController
from transactions.controllers.summary_by_category import SummaryByCategoryController
from transactions.controllers.transaction import TransactionListBulkCreateController
from users.controllers.create_user import UserCreateController
from users.controllers.list_user import UserListController
from users.controllers.retrieve_user import UserRetrieveController
from accounts.controllers.create_account import AccountCreateController

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/create/", UserCreateController.as_view()),
    path("users/", UserListController.as_view()),
    path("users/<str:username>/", UserRetrieveController.as_view()),
    path("accounts/", AccountCreateController.as_view()),
    path("transactions/", TransactionListBulkCreateController.as_view()),
    path("summary/<str:username>/account/", SummaryByAccountController.as_view()),
    path("summary/<str:username>/category/", SummaryByCategoryController.as_view()),
]
