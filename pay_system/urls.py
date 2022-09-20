from django.conf.urls.static import static
from django.conf import settings
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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
