from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():
            #new_user = user_form.save(commit=False)
            #new_user.set_password(user_form.cleaned_data['password']) #set_password 함수를 통해 평문을 암호화
            #new_user.save()
            new_user = user_form.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form':user_form})
