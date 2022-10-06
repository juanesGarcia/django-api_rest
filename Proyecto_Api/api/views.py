
from django.views import View
from .models import Company
from django.http import JsonResponse

# Create your views here.

class CompanyListView(View):
    def get(self, request):
        cList=Company.objects.all()
        return JsonResponse(list(cList.values()),safe=False) #false por que devuelve un array de json no solo un json
    
class CompanyDetailView(View):
    def get(self, request, pk):
        list=Company.objects.get(pk=pk)
        return JsonResponse(list,safe=False) #false por que devuelve un array de json no solo un json
