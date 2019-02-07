from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

@login_required(login_url='/car/login/')
def index(request):

    template = loader.get_template('car/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

    return HttpResponse("Hello, world. You're at the CARS index.")