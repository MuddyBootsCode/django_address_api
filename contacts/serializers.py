from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'slug',
            'first_name',
            'last_name',
            'phone_number',
            'phone_type',
            'street_address1',
            'street_address2',
            'state',
            'zip_code',
        ]
        read_only_fields = [
            'slug'
        ]
