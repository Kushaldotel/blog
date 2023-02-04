from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from .models import Blog, Comment
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    # return HttpResponse("This is Blog")
    return render(request, 'blog/bloghome.html', context)
def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=blog)


    
    # comments = Comment.objects.filter(post=post)
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog/blogpost.html', context)
    # return HttpResponse(f"You are visiting {slug}")

def PostComment(request):
    if request.method=="POST":
        post = Blog.objects.get(slug=request.POST.get('post_id'))
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        print('name', name)
        print(request.POST.get('post_id'))
        comment = Comment(Comment=comment, name=name,post=post)
        comment.save()
        messages.success(request, "You have Successfully commented.")
        return redirect(reverse('blogpost', kwargs={'slug': post.slug}))


def search(request):
    return render(request, 'blog/search.html')

# def contact(request):
#     # return HttpResponse("This is contact")
#     return render(request, 'blog/contact.html')

def main(request):
    return render(request, 'blog/home.html')


# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact form submission',
                f'{message}\n\nFrom: {name} <{email}>',
                'kushaldotel706@gmail.com',
                ['kushaldotel706@gmail.com'],
                fail_silently=False,
            )
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
