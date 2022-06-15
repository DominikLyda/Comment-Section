from django.db import models
from django.contrib.auth.models import User


# model podcastów zawierający nazwe podcastu, opis oraz autora
class Podcasts(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    description = models.TextField()


# model komentarzy zawierający ich treść, przynależność do podcastu oraz użytkownika, który komentarz napisał
class Comments(models.Model):
    text = models.TextField()
    podcast = models.ForeignKey(Podcasts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# model like, który służy do dodawania polubień dla wybranych komentarzy
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)


# model dislike, który służy do dodawania "nie polubień" do wybranych komentarzy
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)