from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request,'blog/post_list.html',{}) # render mette insieme il nostro template blog/post_list.html