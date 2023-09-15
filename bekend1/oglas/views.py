from django.shortcuts import render
from oglas.models import Oglas
import json
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
@api_view(["GET","POST"])
def lista_oglasa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')

            # Create a new instance of YourModel
            new_instance = Oglas(title=title, description=description)
            new_instance.save()

            return JsonResponse({'message': 'Model instance created successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        try:
            instances = Oglas.objects.all()

            data = []
            for instance in instances:
                data.append({
                    'title': instance.title,
                    'description': instance.description,
                    'created_at' : instance.created_at,
                })

            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)