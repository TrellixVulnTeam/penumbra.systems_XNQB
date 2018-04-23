from django.http.response import HttpResponse
from django.template import loader

import DataEntry

def DataEntry(request):
	template = loader.get_template('DataEntry/DataEntry.html')
	output = template.render()
	return HttpResponse(output)
