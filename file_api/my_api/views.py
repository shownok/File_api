from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import FileAll


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def tfileupload(request):
    try:
        tasks = FileAll.objects.all()
        serializer = FileSerializer(tasks, many=True)
        return Response(serializer.data)

    except FileAll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def tCreate(request):
    try:
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    except FileAll.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)


@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))
def update(request, pk):
    tasks = FileAll.objects.get(pk=pk)
    serializer = FileSerializer(tasks, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

