from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("This is Homepage")
    context = {
        'variable1': "This is context checking line",
        "variable2": 23
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")