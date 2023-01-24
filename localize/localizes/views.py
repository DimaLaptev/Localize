from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

'''
unworking render of templates, like this:
def index(request):
    return render(request, 'localizes/index.html')
'''

def index(request):
    output = _('My Test to be translated')
    return HttpResponse(output)
