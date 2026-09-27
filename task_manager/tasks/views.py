from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

from .models import User

from django.shortcuts import get_object_or_404

@api_view(["POST"]) 
def create_user(request):
    serializer = UserSerializer(data=request.data)


    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(["GET"])
def get_users(request):

    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data )


@api_view(["GET"])
def get_user(request, user_id):

    user = get_object_or_404(User, id=user_id)

    serializer = UserSerializer(user)

    return Response(serializer.data)

@api_view(["PUT"])
def update_user(request,user_id):

    user = get_object_or_404(User, id=user_id)
    
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_user(request, user_id):  

    user = get_object_or_404(User, id=user_id)

    user.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
