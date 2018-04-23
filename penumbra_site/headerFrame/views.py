from django.http.response import HttpResponse
from django.template import loader
import subprocess
from subprocess import Popen

def headerFrame(request):
	#p = subprocess.Popen(["start", "cmd", "/k", "{dir}"], shell = True)
	#p.wait()
	template = loader.get_template('headerFrame/headerFrame.html')
	output = template.render()
	return HttpResponse(output)