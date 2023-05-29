from django.shortcuts import render, HttpResponse
# def index1(request):
#     return HttpResponse("awads first succsessful project !")
# def routing(request, num):
#     return HttpResponse(num)
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "hi.html", context)

 