from .models import Onderzoek
from .models import Vraag
from .models import Onderzoekvraag
from .serializers import OnderzoekSerializer
from .serializers import VraagSerializer
from .serializers import OnderzoekvraagSerializer
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def onderzoek_lijst(request, format=None):
    if request.method == 'GET':
        onderzoek = Onderzoek.objects.all()
        serializer = OnderzoekSerializer(onderzoek, many=True)
        return Response({'onderzoeken': serializer.data})

    if request.method == 'POST':
        serializer = OnderzoekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def onderzoek_detail(request, onderzoek_id, format=None):
    try:
        onderzoek = Onderzoek.objects.get(pk=onderzoek_id)
    except Onderzoek.DoesNotExist:
        return Response({'error': 'Onderzoek niet gevonden'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OnderzoekSerializer(onderzoek)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OnderzoekSerializer(onderzoek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        onderzoek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def vragen_lijst(request, format=None):
    if request.method == 'GET':
        vraag = Vraag.objects.all()
        serializer = VraagSerializer(vraag, many=True)
        return Response({'vragen': serializer.data})

@api_view(['GET'])
def onderzoek_vragen_lijst(request, format=None):
    if request.method == 'GET':
        onderzoekvraag = Onderzoekvraag.objects.all()
        serializer = OnderzoekvraagSerializer(onderzoekvraag, many=True)
        return Response({'onderzoekvragen': serializer.data})


@api_view(['POST'])
def login(request):
    return Response({})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test_token(request):
    return Response({})
