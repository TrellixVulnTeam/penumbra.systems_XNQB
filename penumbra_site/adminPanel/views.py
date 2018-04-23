from django.http.response import HttpResponse
from django.template import loader

import adminPanel

def adminPanel(request):
	template = loader.get_template('adminPanel/adminPanel.html')
	output = template.render()
	return HttpResponse(output)
