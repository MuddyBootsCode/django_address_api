from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from contacts.serializers import ContactSerializer
from contacts.models import Contact


# class ContactView(generics.GenericAPIView):
#     serializer_class = ContactSerializer
#     queryset = Contact.objects.all()

class ContactView(APIView):
    """
    Return Contacts
    """

    def get(self, request, *args, **kwargs):
        qs = Contact.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
