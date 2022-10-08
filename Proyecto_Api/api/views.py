
from django.views import View
from .models import Company
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


class CompanyListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request,id=0):#id=0 por que json comienza desde el id=1 entonces 0 lista todas
        if(id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]#por que solo va a devolver 1
                datos={'messagg:':"Success",'companys:': companies}
            else:
                datos={'messagg:':"no found"}
            return JsonResponse(datos)    

        else:
             companies=list(Company.objects.values())
             if len(companies)>0:
                datos={'messagg:':"Success",'companys:': companies}
             else:
                 datos={'messagg:':"Success"}

             return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'],foundation=jd['foundation'])
        datos={'messagg:':"Success"}
        return JsonResponse(datos)

    def put(self, request,id):
         jd=json.loads(request.body)
         companies=list(Company.objects.filter(id=id).values())
         if len(companies)>0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos={'messagg:':"Success"}
         else:
            datos={'messagg:':"no found"}

         return JsonResponse(datos)
    
    def delete(self, request,id):
         companies=list(Company.objects.filter(id=id).values())
         if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos={'messagg:':"Success"}
         else:
            datos={'messagg:':"no found"}
        
         return JsonResponse(datos)



def  list_company(request):
     com= Company.objects.all()
     return render(request,'list_company.html',{'companys':com})

def create_company(request):
    if len(request.POST['name'] and request.POST['website'] and request.POST['foundation']) == 0:
        datos={'messagg:':"no found"}
        return JsonResponse(datos)
    else:
        Company(name=request.POST['name'],website=request.POST['website'],foundation=request.POST['foundation']).save()
        return redirect('/list/')

def delete_company(request,id):
    print('el id es '+str(id))
    Company.objects.filter(id=id).delete()
    return redirect('/list/')


      

def view_update(request,id):
    company=Company.objects.get(id=id)
    
    return render(request, 'update.html',{'com':company})

def update_company(request,id):
     company=Company.objects.get(id=id)
     jd=request.POST
     print(request.POST)
     company.name=jd['name']
     company.website=jd['website']
     company.foundation=jd['foundation']
     company.save()
     return redirect('/list/')
 


