from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.models import User, auth
from .models import Post
from django.contrib import messages
from .create_post_form import CreatePostForm

# Create your views here.


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", {'posts': posts})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    # print(posts[0].subtitle)
    return render(request, 'my_posts.html', {'posts':posts})


def create_post(request):
    if request.method == 'POST':
        # title=request.POST['title']
        # subtitle=request.POST['subtitle']
        # img=request.POST['img']
        # desc=request.POST['desc']

        # post=Post.objects.create_post(title=title,subtitle=subtitle,img=img,desc=desc)
        # post.save()
        # print('hela')
        # return redirect('/')
        form = CreatePostForm(request.POST, request.FILES)

        print("Outside")

        if form.is_valid():
            # print("Inside")
            # print(request.FILES['img'])
            # print(request.user.id)
            # # print("title : " + str(form.cleaned_data['title']))
            # print("img : " + str(form.cleaned_data['img']))
            # print("title : " + str(form.cleaned_data['title']))
            # print("subtitle : " + str(form.cleaned_data['subtitle']))
            # print("desc : " + str(form.cleaned_data['desc']))

            post = Post.objects.create(img=form.cleaned_data['img'], title=form.cleaned_data['title'],
                                       subtitle=form.cleaned_data['subtitle'], desc=form.cleaned_data['desc'], author=request.user)
            # aa = post.save(commit=False)
            # aa.author = request.user
            # aa.save()

            post.save()
            return redirect('/')

    else:
        form = CreatePostForm()

    return render(request, 'create_post.html', {'form': form})


def post(request, id):
    if request.user.is_authenticated:
        blog_data = Post.objects.get(id=id)
        return render(request, "post.html", {'blog_data': blog_data})
    else:
        return redirect('login')
