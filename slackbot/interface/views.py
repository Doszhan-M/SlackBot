from django.views.generic import TemplateView
from django.shortcuts import redirect
import subprocess


class Test(TemplateView):
     template_name = 'interface/base.html'



def test_action(request):
     with open('./scripts/parse.sh', 'rb') as file:
          script = file.read()
     rc = subprocess.call(script, shell=True)
     return redirect('test')
     