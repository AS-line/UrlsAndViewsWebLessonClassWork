from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'О мне'
        return context


class SuperAboutView(AboutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['super_name'] = 'О супер мне'
        return context



def main(request):
    if request.method == 'GET':
        title = request.GET.get('title', 'В тайтл ничего не передали')
        desc = request.GET.get('desc', 'В desc ничего не передали')
        context = {'title': title, 'desc': desc}
        return render(request, 'index.html', context)
    if request.method == 'POST':
        return render(request, 'post2.html', {})


class Main(View):
    def get(self, *args, **kwargs):
        title = self.request.GET.get('title', 'В тайтл ничего не передали')
        desc = self.request.GET.get('desc', 'В desc ничего не передали')
        return render(self.request, 'index.html', {'title': title, 'desc': desc})

    def post(self, *args, **kwargs):
        post_title = self.request.POST.get('post_title', 'пусто')
        post_desc = self.request.POST.get('post_desc', 'пусто')
        return render(self.request, 'post.html', {'post_title': post_title, 'post_desc': post_desc})
