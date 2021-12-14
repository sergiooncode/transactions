"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from transactions.controllers.summary_by_account import SummaryByAccountController
from transactions.controllers.summary_by_category import SummaryByCategoryController
from transactions.controllers.transaction import TransactionListBulkCreateController
from users.controllers.create_user import UserCreateController
from users.controllers.list_user import UserListController
from users.controllers.retrieve_user import UserRetrieveController

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/create", UserCreateController.as_view()),
    path("users/", UserListController.as_view()),
    path("users/<str:username>/", UserRetrieveController.as_view()),
    path("transactions/", TransactionListBulkCreateController.as_view()),
    path("summary/<str:username>/account/", SummaryByAccountController.as_view()),
    path("summary/<str:username>/category/", SummaryByCategoryController.as_view()),
]
