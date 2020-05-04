from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from users.forms import SignupForm


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', CreateView.as_view(
        template_name='signup.html',
        form_class=SignupForm,
        success_url=reverse_lazy('home'),
    ), name='signup'),
]
