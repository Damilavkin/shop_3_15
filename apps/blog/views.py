from django.shortcuts import render

from apps.blog.models import Post


def blog(request):
    blog = Post.objects.all()

    return render(request, "blog/blog.html", context={"blog": blog})

