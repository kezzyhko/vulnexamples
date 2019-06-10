from django.shortcuts import render
from urllib.request import Request, urlopen

from vulnexamples.views import MyFormView
from .forms import BooksForm


class IndexView(MyFormView):
    template_name = 'a9_cve/index.html'
    form_class = BooksForm

    def validate(self, request):
        pass  # TODO

    def on_success(self, request):
        # response = urlopen('http://books_server:8001/%s' % self.form.cleaned_data['path_to_book'])
        req = Request('http://books_server:8001/%s' % self.form.cleaned_data['path_to_book'])
        req.add_header('Range', 'bytes=0-300')
        response = urlopen(req)
        self.headers = response.headers
        self.booktext = response.read().decode()
        return self.render_form(request)

    def render_form(self, request):
        return render(request, self.template_name,
                      {'form': self.form,
                       'headers': getattr(self, 'headers', ''),
                       'booktext': getattr(self, 'booktext', '')})
