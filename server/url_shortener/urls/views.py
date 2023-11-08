from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from urls.forms import URLForm
from urls.models import UrlModel

# Index view, to create the URL
class IndexView(View):
    template_name = 'urls/index.html'
    form_class = URLForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            url_id = ''
            try:
                url_object = UrlModel.objects.get(url=url)
                url_id = url_object.id
            except UrlModel.DoesNotExist:
                url_new = UrlModel(url=url)
                url_new.save()
                url_id = url_new.id
            finally:
                new_url = request.build_absolute_uri() + str(url_id)
                return render(request, self.template_name, {"form": form, 'new_url': new_url})


# Url view, in charge of looking in database and redirecting to the real URL
class RedirectView(View):
    def get(self, request, id):
        try:
            url_object = UrlModel.objects.get(pk=id)
        except Exception as e:
             raise Http404("The URL does not exist")
        return redirect(url_object.url)