# blog/views.py
import os
import logging
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import redirect
from .forms import PostForm
from .models import BlogPost
from django.shortcuts import render
from django.conf import settings


# Set up logging
LOGGING_DIR = os.path.join(settings.BASE_DIR, 'logs')
os.makedirs(LOGGING_DIR, exist_ok=True)

LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
LOG_FILE = os.path.join(LOGGING_DIR, 'views.log')

logging.basicConfig(
    level=LOGLEVEL,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger(__name__)


def notebook_view(request):
    logger.debug('Debug message for testing logging inside of Notebook view.')
    return render(request, 'blog/notebook_view.html')


def jupyterlite_view(request):
    logger.debug('Debug message for testing logging inside of Jupyter Lite view.')
    # Link to your local JupyterLite Notebook
    local_jupyterlite_url = 'http://127.0.0.1:8000/viewer?repo=notebooks/mini_project_1.ipynb'

    # Pass the local JupyterLite URL to the template
    context = {'jupyterlite_url': local_jupyterlite_url}
    return render(request, 'blog/jupyterlite_view.html', context)


def post_view(request):
    # Assuming 'blog' is your app name
    template_dir = os.path.join('..', 'templates', 'blog', 'posts')

    # Check if the directory exists
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)

    templates = [f for f in os.listdir(template_dir) if f.endswith('.html')]
    logger.info(f'Templates found: {templates}')

    return render(request, 'blog/post.html', {'templates': templates})


def blog_index_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


@login_required
def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Ensure the user is logged in
            if request.user.is_authenticated:
                author = request.user
            else:
                # Handle the case where the user is not authenticated (you can redirect to login or handle it differently)
                messages.error(request, 'You need to be logged in to create a blog post.')
                return redirect('login')

            # Save blog post to the database
            BlogPost.objects.create(title=title, content=content, author=author)

            # Create the directory if it doesn't exist
            posts_directory = "templates/blog/posts/"
            os.makedirs(posts_directory, exist_ok=True)

            # Create a new HTML file
            file_path = os.path.join(posts_directory, f"{title}.html")
            with open(file_path, 'w') as file:
                file.write(f"<html><head><title>{title}</title></head><body>{content}</body></html>")

            return redirect('blog_index')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})


def detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


def base_view(request):
    return render(request, 'base.html')


def index_view(request):
    return render(request, 'index.html')


def register_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == "POST":
        if not username:
            messages.error(request, 'Username is required.')
        elif not password:
            messages.error(request, 'Password is required.')
        else:
            try:
                new_user = User.objects.create_user(username=username)
                new_user.set_password(password)
                new_user.save()
            except IntegrityError:
                messages.error(request, f'User {username} is already registered.')
            else:
                return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == "POST":
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the index page or any other page after logout

