from django.shortcuts import render

def home(request):
    return render(request,'./home.html')

def comercial(request):
    return render(request,'comercial.html')

def farma(request):
    return render(request,'farma.html')

def hospitalar(request):
    return render(request,'hospitalar.html')

def academiaec(request):
    return render(request,'academiaec.html')

