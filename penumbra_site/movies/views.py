from django.http.response import HttpResponse
from django.template import loader
from .models import Movie

import movies

def movies(request):
	movies_all = Movie.objects.all().order_by('-slug')
	template = loader.get_template('movies/movies.html')
	output = template.render({'movies': movies_all})
	return HttpResponse(output)