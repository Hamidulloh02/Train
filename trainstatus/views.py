from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import IshHolati,Yulak, Stansiyalar
from .serializers import IshHolatiSerializers, IshHolati, StansiyaSerializers, YulakSerializers
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class WorkStatus(ListAPIView):
    queryset = IshHolati.objects.all()
    serializer_class = IshHolatiSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    filterset_fields = ['yuklanganvagon', 'yuklanishunturganvagon', 'tushurilganvagonlar']
    filter_backends = [filters.SearchFilter]
    search_fields = ['yuklanganvagon', 'yuklanishunturganvagon', 'tushurilganvagonlar']



class WorkStatusAdd(CreateAPIView):
    queryset = IshHolati.objects.all()
    serializer_class = IshHolatiSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]

class WorkStatusDelete(RetrieveUpdateDestroyAPIView):
    queryset = IshHolati.objects.all()
    serializer_class = IshHolatiSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]




class YulakListView(ListAPIView):
    queryset = Yulak.objects.all()
    serializer_class = YulakSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    filterset_fields = ['stansiya', 'stansiya']
    filter_backends = [filters.SearchFilter]
    search_fields = ['stansiya', 'stansiya']


class YulakEditView(RetrieveUpdateDestroyAPIView):
    queryset = Yulak.objects.all()
    serializer_class = YulakSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    filterset_fields = ['stansiya', 'stansiya']
    filter_backends = [filters.SearchFilter]
    search_fields = ['stansiya', 'stansiya']


class YulakAdd(CreateAPIView):
    queryset = Yulak.objects.all()
    serializer_class = YulakSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]


class StanssiyaView(ListAPIView):
    queryset = Stansiyalar.objects.all()
    serializer_class = StansiyaSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    filterset_fields = ['nomi']
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomi']
