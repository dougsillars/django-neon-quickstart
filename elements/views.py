from django.shortcuts import render
from .models import Element
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK")

def elements_list(request):
    elements = Element.objects.all() 
    return render(request, 'elements_list.html', {'elements': elements})

@csrf_exempt
def element_delete(request, item_id):
    el = Element.objects.get(id = item_id)

    el.delete()

    elements = Element.objects.all() 

    return render(request, 'elements_list.html', {'elements': elements})
