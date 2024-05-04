from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/",include("user.urls")),
    path("products/",include("products.urls")),
    path("category/",include("category.urls")),
    path("order/",include("order.urls")),
    path("cart/",include("cart.urls")),
    path("cart/",include("payment.urls")),
    

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
