
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

import apiApp.views as views

urlpatterns = [
     path('start_payment', views.start_payment, name="start_payment"),
    path('success', views.handle_payment_success, name="success")
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
