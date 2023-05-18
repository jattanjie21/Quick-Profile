from django.shortcuts import render 



def template1_index(request):
    return render(request, 'template_1/base/index.html',)