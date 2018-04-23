from django.http.response import HttpResponse

# Create your views here.
from .models import Tag


def homepage(request):
	tag_list = Tag.objects.all()
	template = loader.get_template('errors/errors.html')
	context = Context({'tag_list': tag_list})
	output = template.render(context)
    return HttpResponse(output)