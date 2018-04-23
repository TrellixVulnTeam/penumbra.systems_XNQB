from django.http.response import HttpResponse
from django.template import loader

def demoscene(request):
	template = loader.get_template('demoscene/demoscene.html')
	output = template.render()
	return HttpResponse(output)
