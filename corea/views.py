from django.shortcuts import render



def frontpage(request):
    return render(request,'corea/frontpage.html')

def about(request):
    return render(request,'corea/about.html')