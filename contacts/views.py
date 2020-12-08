from rest_framework import generics
from contacts.serializers import ContactSerializer
from contacts.models import Contact
from django_filters.rest_framework import DjangoFilterBackend


class ContactListView(generics.ListAPIView):
    """
    Returns a list view of contacts filterable by each contact field
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name", "phone_number", "phone_type", "street_address1", "street_address2",
                        "city", "state", "zip_code"]


class ContactCreateView(generics.CreateAPIView):
    """
    Allows the user to create a contact
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactSlugView(generics.RetrieveAPIView):
    """
    Allows the user to select a contact by slug
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'slug'


class ContactEditView(generics.UpdateAPIView):
    """
    Allows the user to edit a contact
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'slug'


class ContactDeleteView(generics.DestroyAPIView):
    """
    Allows the user to delete a contact
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'slug'
