from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)

    print "INDEX"
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})
     
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)

    print "POST"
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

    #return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))