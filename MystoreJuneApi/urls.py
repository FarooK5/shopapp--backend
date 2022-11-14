
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter
from api import views
router=DefaultRouter()

router.register("products",views.ProductsView,basename="products")

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('token/', ObtainAuthToken.as_view()),
     path("",include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
