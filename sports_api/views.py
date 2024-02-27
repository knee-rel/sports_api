from django.http import JsonResponse
from django.shortcuts import render
from .models import Sport
from .serializers import SportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Decorator to describe the function, for documentation purposes
# this means that the function accepts both POST and GET requestsz


@api_view(['GET', 'POST'])
def sport_list(request, format=None):
    # get the sports
    # serialize them
    # return json

    if request.method == 'GET':
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return render(request, 'sport_list.html', {'sports': serializer.data})

    if request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def sport_detail(request, id, format=None):
    try:
        sport = Sport.objects.get(pk=id)
    except Sport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SportSerializer(sport)
        return render(request, 'sport_detail.html', {'sport': serializer.data})
    elif request.method == 'PUT':
        serializer = SportSerializer(sport, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
