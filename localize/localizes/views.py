from django.shortcuts import render
from django.utils.translation import ugettext as _


def index(request):
    context = {
            'test': _('This is the test'),
            'variable': _('This is a variable'),
            }
    return render(request, 'localizes/index.html', context)
