from django.contrib import admin
from django.urls import path, include
from contacts.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContactView.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls'))
]
