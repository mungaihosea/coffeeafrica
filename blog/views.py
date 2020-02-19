from django.shortcuts import render

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def blog_single(request, id):
    context = {}
    return render(request, 'blog_single.html', context)