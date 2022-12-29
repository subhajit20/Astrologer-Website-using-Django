from django.shortcuts import render


def Home(request):
    return render(request,'Home.html')

def Kundali(request):
    return render(request,'GetYourFreeKundali.html')

def KundaliMatching(request):
    return render(request,'KundaliMatching/KundaliMatching.html')

def Askyourastrologer(request):
    return render(request,'askyourastrologer/AskYourAstrologer.html')

def Blogpage(request):
    return render(request,'BlogPage/Blog.html')

