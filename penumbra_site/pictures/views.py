from django.http.response import HttpResponse
from django.template import loader

from .models import Picture

import pictures
import os

def pictures(request):
	pictures_all = Picture.objects.all().order_by('-slug')
	template = loader.get_template('pictures/pictures.html')
	output = template.render({'pictures': pictures_all})
	##os.system("start /B start cmd.exe @cmd /k dir")
	return HttpResponse(output)