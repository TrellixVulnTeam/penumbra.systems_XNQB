from django.http.response import HttpResponse
from django.template import loader

import contactme

def contactme(request):
	template = loader.get_template('contactme/contactme.html')
	output = template.render()
	return HttpResponse(output)