from django.test import SimpleTestCase
from django.urls import reverse, resolve
from page.views import PodcastList, PodcastComments, AddPodcast, Account


class TestUrls(SimpleTestCase):

    def test_podcasty_url_is_resolved(self):
        url = reverse('podcasty')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PodcastList)

    def test_komentarze_url_is_resolved(self):
        url = reverse('komentarze', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PodcastComments)

    def test_dodaj_podcast_url_is_resolved(self):
        url = reverse('dodaj podcast')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddPodcast)

    def test_konto_url_is_resolved(self):
        url = reverse('konto')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Account)
