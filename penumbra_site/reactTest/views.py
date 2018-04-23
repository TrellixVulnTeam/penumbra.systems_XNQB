from django.http.response import HttpResponse
from django.template import loader
from django.utils import timezone

import reactTest

def reactTest(request):
	template = loader.get_template('reactTest/reactTest.html')
	output = template.render()
	return HttpResponse(output)