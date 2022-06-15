from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Podcasts, Comments, User, Like, Dislike
from .forms import NewUserForm, CommentForm, PodcastForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


# Widok paska menu u góry ekranu
def homepage(request):
    return render(request, 'base.html')


# Widok służący do rejestracji użytkownika, wykorzystujący crispy forms i bootstrap templates
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("http://127.0.0.1:8000/login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# Widok służący do logowania użytkownika, wykorzystujący crispy forms i bootstrap templates
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("http://127.0.0.1:8000")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


# Widok służący do wylogowania użytkownika i przeniesienia go na stronę główną
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("http://127.0.0.1:8000")


# Widok służący do wyświetlania pełnej listy podcastów z modelu Podcasts
class PodcastList(View):
    def get(self, request):
        podcast_list = Podcasts.objects.all()
        context = {'podcast_list': podcast_list}
        return render(request, 'podcasts.html', context)


# Widok służący do wyświetlania listy komentarzy przypisanej do wybranego podcastu oraz
# umożliwiający komentowanie zalogowanym użytkownikom
class PodcastComments(View):
    def get(self, request, podcast_id):
        form = CommentForm()
        podcast = Podcasts.objects.get(id=podcast_id)
        comments = Comments.objects.filter(podcast=podcast)

        context = {'podcast': podcast,
                   'form': form,
                   'comments': comments}
        return render(request, 'podcast_comments.html', context)

    def post(self, request, podcast_id):
        form = CommentForm(request.POST)
        podcast = Podcasts.objects.get(id=podcast_id)
        context = {'podcast': podcast,
                   'form': form}
        if form.is_valid():
            comment = form.cleaned_data['comment']
            user = request.user
            podcast = podcast
            try:
                Comments.objects.create(text=comment, podcast=podcast, user=user)
            except ValueError:
                return redirect("http://127.0.0.1:8000/login")
            return redirect(f"http://127.0.0.1:8000/podcasty/{podcast_id}")
        return render(request, 'podcast_comment.html', context)


# Widok służący do usuwania komentarzy, wyświetlający potwierdzenie usunięcia i przenoszący na listę podcastów
def delete_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)

    if request.method == 'POST':
        comment.delete()
        return redirect('http://127.0.0.1:8000/podcasty')

    return render(request, 'delete-comment.html', {'comment': comment})


# Widok służący do wyświetlania statystyk przypisanych do konta oraz wszystkich napisanych przez użytkownika komentarzy
# dostępny tylko dla zalogowanych użytkowników
@method_decorator(login_required, name='dispatch')
class Account(View):
    def get(self, request):
        try:
            user = request.user
            comments = Comments.objects.filter(user=user)
            context = {'user': user,
                       'comments': comments}

            return render(request, 'account.html', context)
        except TypeError:

              return redirect("http://127.0.0.1:8000/login")


# Widok służący do dodawania podcastów, dostępny tylko dla super_user'a
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AddPodcast(View):

    def get(self, request):
        form = PodcastForm()
        context = {'form': form }
        return render(request, 'add-podcast.html', context)

    def post(self, request):
        form = PodcastForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            Podcasts.objects.create(name=name, author=author, description=description)
            return redirect("http://127.0.0.1:8000/podcasty/")
        return render(request, 'add-podcast.html', context)


class About(View):
    def get(self, request):
        pass
