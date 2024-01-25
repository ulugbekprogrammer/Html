from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeview(request):
    print(str(request))
    return render(request=request, template_name='index.html', context={})

def mssview(request):
    return HttpResponse('Bu mss view edi')