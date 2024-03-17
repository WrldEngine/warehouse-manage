from django.contrib import admin
from django.urls import path, include

from market.views import ProductListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/order/", ProductListView.as_view()),
]
