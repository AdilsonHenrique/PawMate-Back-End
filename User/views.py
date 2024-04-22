from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import PerfilPawmateForm, UserCreateForm
from .models import PerfilPawmate

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('sucesso')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()

        perfil = PerfilPawmate.objects.create(
            usuario=user,
            nome_dono=form.cleaned_data['username'],
            cidade_dono='',
            estado_dono='',
            pais_dono='',
            telefone_dono='',
            nome_animal='',
            idade_animal=0,
            raca_animal=''
        )

        return super().form_valid(form)
