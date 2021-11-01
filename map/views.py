from django.shortcuts import render


def kakao(request):
    return render(request,'kakao.html')

def google(request):
    return render(request,'google.html')
