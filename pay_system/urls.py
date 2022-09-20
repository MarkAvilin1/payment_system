from django.contrib import admin
from django.urls import path

from . import views
from store import views as vs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', vs.store, name='store'),
    path('item/<int:pk>/', vs.product_detail, name='product_detail'),
    path('buy/<int:pk>', vs.buy, name='buy'),
    path('payment/<int:pk>', vs.payment, name='payment'),
    path('success/', vs.success, name='success'),
    path('wrong/', vs.wrong, name='wrong'),
]
