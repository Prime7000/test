from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from re import X, template
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView,FormView
# from .models import Post
# from .form import PostForm
# from django.contrib import messages
import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')





# Create your views here.
class HomePageView(TemplateView):
        template_name = 'web.html'



class Calculus1(TemplateView):
    #template_name = 'calculus_form.html'
    def get(self, request):
        return render(request, 'calculus_form.html')

    def post(self, request):
        x = request.POST.get('x')
        respect = request.POST.get('respect')
        order = int(request.POST.get('order'))
        equ = x 
        result = sympy.diff(equ, respect, order)
        return render(request, 'calculus_form.html', {'result': result})

class Algebra1(TemplateView):
    # template_name = 'algebra_form.html'
    def get(self, request):
        return render(request, 'algebra_form.html')

    def post(self, request):
        x = request.POST.get('x')
        print("x:", x)
        result = sympy.simplify(x)
        return render(request, 'algebra_form.html', {'result': result})



class Probability1(TemplateView):
    # template_name = 'probability_form.html'

    def get(self, request):
        return render(request, 'probability_form.html')

    def post(self, request):
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        print('x, x')
        print('y:' ,y)


        ans = x/y
        result = ans
        return render(request, 'probability_form.html', {'result': result})




class Statictics1(TemplateView):
    # template_name = 'statistic_form.html'

    def get(self, request):
        return render(request, 'statistic_form.html')

    def post(self, request):
        x = request.POST.get('x')
        
        list = x.split()

        sorted_numbers = sorted(list)
        length = len(sorted_numbers)

        if length % 2 == 0:
            mid1 = sorted_numbers[length // 2]
            mid2 = sorted_numbers[length // 2 - 1]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_numbers[length // 2]

        result = median

        return render(request, 'statistic_form.html', {'result': result})


print('#########################################')

class Calculus2(TemplateView):
    template_name = 'calculus1.html'

class Algebra2(TemplateView):
    template_name = 'algebra1.html'

class Probability2(TemplateView):
    template_name = 'probability1.html'

class Statistics2(TemplateView):
    template_name = 'statistics1.html'

class About(TemplateView):
    template_name = 'about.html'
