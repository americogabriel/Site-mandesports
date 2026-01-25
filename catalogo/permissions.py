from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class SuperAdminRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('url_home')

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        
        messages.warning(request," Você não tem premissão para acessar essa página ")
        return redirect('url_home')
            
