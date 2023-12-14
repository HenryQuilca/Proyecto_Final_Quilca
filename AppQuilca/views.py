from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from AppQuilca.forms import BusquedaRaquetaForm, UserRegisterForm, UserUpdateForm, AvatarUpdateForm, ComentarioForm
from AppQuilca.models import Racquet, Avatar, Comments


# Create your views here.
def home(request):
    contexto = {}
    return render(request, "base1.html", contexto)


def about_me(request):
    contexto = {}
    return render(request, "AppQuilca/about_me.html", contexto)


def buscar_racquet(request):
    racquet = request.GET["raqueta"]
    raquetas = Racquet.objects.filter(raqueta__icontains=racquet)
    contexto = {
        "raquetas": raquetas,
        "form": BusquedaRaquetaForm(),
    }
    return render(request, 'AppQuilca/buscar_racquets.html', contexto)


class RacquetCreate(LoginRequiredMixin, CreateView):
    model = Racquet
    success_url = reverse_lazy('RacquetList')
    template_name = "AppQuilca/crear_raqueta.html"
    fields = ["raqueta", "precio", "estado", "fecha_creacion", "stock", "descripcion", "imagen"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.fecha_creacion = timezone.now()
        return super().form_valid(form)


class RacquetList(ListView):
    model = Racquet
    template_name = "AppQuilca/list_racquets.html"


class RacquetDetail(DetailView):
    model = Racquet
    template_name = "AppQuilca/details_racquets.html"


class RacquetUpdate(LoginRequiredMixin, UpdateView):
    model = Racquet
    success_url = "/app/listar_raquetas"
    template_name = "AppQuilca/update_racquets.html"
    fields = ["raqueta", "precio", "estado", "fecha_creacion", "stock", "descripcion", "imagen"]


class RacquetDelete(LoginRequiredMixin, DeleteView):
    model = Racquet
    template_name = "AppQuilca/delete_racquets.html"
    success_url = "/app/listar_raquetas"


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('Home')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "AppQuilca/login.html", contexto)


def sing_up(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("RacquetList")

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "AppQuilca/singup.html", contexto)


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":

        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.last_name = data["last_name"]
            user.first_name = data["first_name"]
            user.save()
            return redirect("RacquetList")

    form = UserUpdateForm(initial={"email": user.email, "last_name": user.last_name, "first_name": user.first_name})
    contexto = {
        "form": form,
    }
    return render(request, "AppQuilca/edit_profile.html", contexto)


@login_required
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("RacquetList")

    form = AvatarUpdateForm()
    contexto = {
        "form": form,
    }
    return render(request, "AppQuilca/avatar.html", contexto)


class CommentCreate(CreateView):
    model = Comments
    fields = ["comentario"]
    template_name = 'AppQuilca/comentario.html'
    success_url = reverse_lazy('RacquetList')

    def form_valid(self, form):
        raqueta = get_object_or_404(Racquet, id=self.kwargs['raqueta_id'])
        form.instance.raqueta = raqueta
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class CommentList(ListView):
    model = Comments
    template_name = 'AppQuilca/list_racquets.html'
    context_object_name = "comentarios"

