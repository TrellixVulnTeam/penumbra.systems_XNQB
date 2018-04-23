from django.http.response import HttpResponse
from django.template import loader

def libraries(request):
	template = loader.get_template('libraries/libraries.html')
	output = template.render()
	return HttpResponse(output)