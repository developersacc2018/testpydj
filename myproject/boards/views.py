from django.shortcuts import render

boards = [1,2,3,4,5,6,7,8]
def home(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'home.html', {'boards': boards})
def service(request):
#return HttpResponse('Hello, World!')
    return render(request, 'service.html', {'boards': boards})
def about(request):
#return HttpResponse('Hello, World!')
    return render(request, 'about.html', {'boards': boards})
def contact(request):
#return HttpResponse('Hello, World!')
    return render(request, 'contact.html', {'boards': boards})