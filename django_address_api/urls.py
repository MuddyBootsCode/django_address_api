from django.contrib import admin
from django.urls import path, include
from contacts.views import ContactCreateView, ContactListView, ContactSlugView, ContactEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', ContactListView.as_view(), name='test'),
    path('create_contact/', ContactCreateView.as_view(), name='create'),
    path('contacts/<slug:slug>', ContactSlugView.as_view(), name='slug_view'),
    path('edit_contact/<slug:slug>', ContactEditView.as_view(), name='edit_view'),
    path('api-auth/', include('rest_framework.urls'))
]
