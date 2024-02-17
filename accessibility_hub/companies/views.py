from .models import Onderzoek
from .serializers import OnderzoekSerializer
from rest_framework.decorators import api_view
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
