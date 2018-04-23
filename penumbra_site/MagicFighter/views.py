from django.http.response import HttpResponse
from django.template import loader, RequestContext
from django.views.decorators.cache import never_cache
from django.shortcuts import render

@never_cache
def MagicFighter(request):
	#template = loader.get_template('MagicFighter/MagicFighter.html')
	#c = RequestContext(request, { 'object_list': MagicFighter.objects.all() })
	#output = template.render(c)
	#return HttpResponse(output)
	return render(request, 'MagicFighter/MagicFighter.html')