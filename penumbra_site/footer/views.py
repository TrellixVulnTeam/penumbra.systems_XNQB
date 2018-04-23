from django.http.response import HttpResponse
from django.template import loader

def footer(request):
	template = loader.get_template('footer/footer.html')
	output = template.render()
	return HttpResponse(output)