from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Uzduotis

# Create your views here.
def index(request):
    return render(request, 'index.html')


class UzduotysListView(LoginRequiredMixin, generic.ListView):
    model = Uzduotis
    template_name = 'manouzduotys.html'
    paginate_by = 4

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user)


class UserUzduotisCreateView(LoginRequiredMixin, generic.CreateView):
    model = Uzduotis
    fields = ['uzduotis']
    success_url = '/todo/manouzduotys'
    template_name = 'user_uzduotis_form.html'

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)


class UzduotisUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Uzduotis
    fields = ['uzduotis']
    success_url = '/todo/manouzduotys'
    template_name = 'user_uzduotis_form.html'

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)


class UzduotisDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Uzduotis
    success_url = '/todo/manouzduotys'
    template_name = 'trinimas_form.html'

    def form_valid(self, form):
        form.vartotojas = self.request.user
        return super().form_valid(form)

