from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class User(View):
    def post(self, request):
        decoded = request.body.decode("utf-8")
        data = json.loads(decoded)
        name = data.get('name')
        vk_id = data.get('vk_id')

        user_data = {
            'name': name,
            'vk_id': vk_id,
        }

        user = User.objects.create(**user_data)

        data = {
            "message": f"New user created with  id: {user.id}"
        }
        return JsonResponse(data, status=201)
