from django.shortcuts import render

# Create your views here.

def index(request):
    if request=='POST':
        city=request.POST['city']

    else:
        city=''
    
    return render(request, 'index.html',{{'city':city}})
