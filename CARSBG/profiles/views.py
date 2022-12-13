from django.contrib.auth import get_user_model, views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from CARSBG.cars.models import Car

from CARSBG.profiles.forms import UserCreateForm

# Create your views here.
UserModel = get_user_model()

UserCreationForm = UserCreateForm


class RegisterView(views.CreateView):
    template_name = 'profiles/register.html'
    model = UserModel
    form_class = UserCreationForm
    success_url = reverse_lazy('index')


class LoginView(auth_views.LoginView):
    template_name = 'profiles/login.html'


class ProfileDetails(views.DetailView):
    template_name = 'profiles/details.html'
    model = UserModel

    def cars_listed(self, user):
        cars_listed = len(Car.objects.filter(user=user))
        return cars_listed

    def get_context_data(self, **kwargs):
        context = super(ProfileDetails, self).get_context_data(**kwargs)
        user = UserModel.objects.get(id=self.kwargs['pk'])
        context['car_listed'] = self.cars_listed(user)
        context['user'] = user
        return context


class ProfileEdit(views.UpdateView):
    template_name = 'profiles/edit-profile.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'profile_picture', 'username')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={
            'pk': self.request.user.id
        })


class DeleteProfile(views.DeleteView):
    template_name = 'profiles/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        self.request.user.delete()


class LogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
