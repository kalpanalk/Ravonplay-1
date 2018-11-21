from django.shortcuts import render, redirect
#views here
def index(request):
    context = {}
    return render(request, 'index.html', context)
def signin(request):
    context = {}
    return render(request, 'signin.html',context)