from django.http.response import HttpResponse
from django.template import loader

def links(request):
	template = loader.get_template('links/links.html')
	output = template.render()
	return HttpResponse(output)