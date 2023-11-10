from django.shortcuts import render, redirect
from . forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = UserForm()
    context = {
        'form': form,
        'email_error': form.errors.get('email'),
        'password_error': form.errors.get('password'),
        'confirm_password_error': form.errors.get('confirm_password')
    }
    return render(request, 'users/register.html', context=context)
