from django.shortcuts import render
from django.views import View

# Create your views here.


class MainSiteView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'conf_template.html', ctx)
