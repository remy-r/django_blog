from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'accueil/index.html')


class ErrorView(TemplateView):
    template_name = "accueil/error.html"
    error_name = None
    error_message = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['error_name'] = self.error_name
        context['error_message'] = self.error_message
        return context


def raise_message(request, name="", message=""):
    error = ErrorView
    error.error_name = name
    error.error_message = message
    return error.as_view()(request)

