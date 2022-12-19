
from rest_framework import generics, status
from rest_framework.response import Response
from .import serializers


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello user "}, status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreateSerializer

    def post(self, request):
        data = request.data


        serializers = self.serializer_class(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)

        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)