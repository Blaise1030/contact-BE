from contacts.serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from contacts.models import Contact
from rest_framework import status


# Create your views here.

# This is to get all contacts

@api_view(['GET'])
def get_all_products(_):
    contacts = Contact.objects.all()
    serializedContacts = ContactSerializer(contacts, many=True)
    return JsonResponse({
        'results': serializedContacts.data
    })


# Create Contacts
@api_view(['POST'])
def createContact(request):
    serialized = ContactSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# Edit, delete or put contact

@api_view(['GET', 'PUT', 'DELETE'])
def contact(request, id):

    try:
        contact = Contact.objects.get(pk=id)
        if request.method == 'GET':
            return getAContact(request, contact)
        elif request.method == 'PUT':
            return putAContact(request, contact)
        elif request.method == 'DELETE':
            return deleteAContact(request, contact)
        else:
            return JsonResponse({'message': 'Method not allowed'})
    except Contact.DoesNotExist:
        return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


def getAContact(_, contact):
    serializedContacts = ContactSerializer(contact)
    return Response(serializedContacts.data, status=status.HTTP_200_OK)


def putAContact(request, contact):
    serializedContacts = ContactSerializer(contact, data=request.data)
    if serializedContacts.is_valid():
        serializedContacts.save()
        return Response(serializedContacts.data)
    return Response(serializedContacts.errors, status=status.HTTP_400_BAD_REQUEST)


def deleteAContact(_, contact):
    contact.delete()
    return Response({'details': 'Contact is deleted'}, status=status.HTTP_204_NO_CONTENT)
