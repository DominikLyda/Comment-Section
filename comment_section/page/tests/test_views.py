from django.test import TestCase, Client
from django.urls import reverse
from page.models import Podcasts, Comments
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.podcasty_url = reverse('podcasty')
        self.komentarze_url = reverse('komentarze', args=['420'])
        self.last_comment = Comments.objects.first()
        self.podcast = Podcasts.objects.create(
            id=420,
            name='Testowy Podcast',
            author='Testowy autor',
            description='Testowy opis=Testowy opis=Testowy opis'
        )

    def test_podcast_list_GET(self):
        response = self.client.get(self.podcasty_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'podcasts.html')

    def test_podcast_comments_GET(self):
        response = self.client.get(self.komentarze_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'podcast_comments.html')

    def test_podcast_comments_POST_add_new_comment(self):

        response = self.client.post(self.komentarze_url, {
            'comment': 'przykładowy komentarz testowy',
            'podcast': self.podcast,
            'user': self.client
        })

        self.assertEquals(response.status_code, 302)
        # self.assertEquals(self.last_comment.podcast, self.podcast)

