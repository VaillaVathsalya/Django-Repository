# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

# Create your views here.
