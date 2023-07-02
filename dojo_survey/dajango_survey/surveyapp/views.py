from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request, 'index.html')
def index2(request):
    if request.method=='POST':
        name = request.POST['name']
        city = request.POST['city'] 
        language = request.POST['language']
        comment = request.POST['comment']
        context = {
            "name":name,
            "language":language,
            "comment":comment,
            "city":city
        }
        return render(request,'index2.html',context)

