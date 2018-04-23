from django.http.response import HttpResponse
from django.template import loader

def splashPage(request):
	template = loader.get_template('splashPage/splashPage.html')
	output = template.render()
	return HttpResponse(output)
# Create your views here.
