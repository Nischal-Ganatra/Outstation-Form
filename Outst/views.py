from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Info, Approved


def Hey(request):
    return render(request, 'Outst/welcome.html')


# Create your views here.
class NewForm(CreateView):
    model = Info
    fields = ['name', 'roomno', 'bitsid', 'destination', 'leavingdate', 'returningdate']


def thankyou(request):
    return render(request, 'Outst/thankyou.html')


class UserFormView(View):

    form_class = UserForm
    template_name = 'Outst/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # request.user.username       display their username
                    return redirect('Outst:hey')
        return render(request, self.template_name, {'form': form})

error = False


class LoginForm(View):

    form_class = UserForm
    template_name = 'Outst/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        if error:
            return render(request, self.template_name, {'form': form}, {'error': error})
        else:
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            if user.is_staff:
                return HttpResponseRedirect("/outst/list/")
            else:
                return HttpResponseRedirect("/outst/hey/")
        else:
            # Show an error page
            error = True
            return HttpResponseRedirect("/outst/", {'error': error})


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/outst/")


class IndexView(generic.ListView):
    template_name = 'Outst/index.html'

    def get_queryset(self):
        return Info.objects.all()


class DetailView(generic.DetailView):
    model = Info
    template_name = 'Outst/detail.html'


class ItemAdd(CreateView):
    model = Approved
    fields = ['name', 'accepted', 'date', 'mealtype']
    template_name = 'Outst/add_to_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = Info.objects.get(pk=product_pk)
        context.update({
            'product': product
        })
        return context


class AppIndexView(generic.ListView):
    template_name = 'Outst/Appindex.html'

    def get_queryset(self):
        return Approved.objects.all()


