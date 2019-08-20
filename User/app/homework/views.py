from django.shortcuts import render
from django.views import View
import requests
from .models import User
import json
from django.http import HttpResponse
from app.homework.helpers import make_requests
from app.homework.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class UserView(View):
    def get(self, request, *args, **kwargs):
        data = []
        BASE_URL = 'https://randomuser.me/api/?results=200'
        response = make_requests(BASE_URL)
        print(response)
        if response:
            #response = json.dumps(response)
            print(type(response))
            results = response['results']
            for result in results:
                name = result['name']['first']
                lastname = result['name']['last']
                data.append(User(
                name=name,
                lastname=lastname
            ))
            User.objects.bulk_create(data)
            queryset=User.objects.all()
            serializer = UserSerializer(queryset, many=True)
        return HttpResponse(serializer.data)
