from django.shortcuts import render
from django.http import JsonResponse


def test_view(request):  # Step 1
    data = {
        'name': 'john',
        'age': 23
    }
    return JsonResponse(data)
