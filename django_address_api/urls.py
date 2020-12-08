from django.contrib import admin
from django.urls import path, include
from contacts.views import ContactCreateView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContactView.as_view(), name='test'),
    path('create/', ContactCreateView.as_view(), name='create'),
    path('api-auth/', include('rest_framework.urls'))
]
