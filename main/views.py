from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ElementoView(TemplateView):
    template_name = 'elemento.html'