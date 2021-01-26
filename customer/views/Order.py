from django.shortcuts import render
from django.views import View
# Create your views here.


class Order(View):
    def get(self,request,*args,**kwargs):
        #get every item from each category



        #pass to the context


        #return
        return render(request,'customer/index.html')