from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# define a function called login_view that takes request from user


def login_view(request):
    error_message = None
    form = AuthenticationForm()

    # when user hist login, post request is generated
    if request.method == 'POST':
        # read data sent by form via post request
        form = AuthenticationForm(data=request.POST)

        # check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # use Django's authenticate function to validate user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('sales:records')

        else:
            error_message = 'well, that did not work :/'

    # prepare data to send from view to template
    context = {
        'form': form,
        'error_message': error_message
    }

    # load login page using context info
    return render(request, 'auth/login.html', context)


# define logout_view function
def logout_view(request):
    logout(request)
    return redirect('login')
