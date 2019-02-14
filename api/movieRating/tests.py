from django.test import TestCase
from .models import Movie
from rest_framework.test import APITestCase, APIClient
from .serializers import MovieSerializer

# Create your tests here.

class BaseViewsTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_movie(title="", director=""):
        if title != "" and director != "":
            Movies.objects.create(title=title, director=director)

    def setUp(self):
        self.create_movie('The Dark Knight', 'Cristopher Nolan')
        self.create_movie('The lord of the Rings', 'Peter Jackson')
        self.create_movie('Star Wars', 'George Lucas')

class getAllMovies(BaseViewsTest):
    
    def test_get_all_movies(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        expected = Movies.objects.all()
        serialized = MovieSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
