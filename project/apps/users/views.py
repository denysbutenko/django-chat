from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from .forms import SignUpForm, SignInForm


def signin_view(request):
    form = SignInForm()
    context = {}
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username", None)
            password = form.cleaned_data.get("password", None)
            user = authenticate(username=username, password=password)

        context["form"] = form

        if not user:
            # User NOT EXISTS
            messages.error(request, _(u"User is not exist. Try again."))
        else:
            # User SIGNED IN
            login(request, user)

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('/')
    else:
        form = SignInForm()
        context["form"] = form
        if request.user.is_authenticated():
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect(reverse("chat:index"))
    return render_to_response('users/signin.html', context,
                              context_instance=RequestContext(request))


def signup_view(request):
    if request.user.is_authenticated():
        return redirect(reverse("index"))

    form = SignUpForm()
    context = {}

    register_data = request.session.get('register_data', False)
    if register_data:
        form = SignUpForm(initial=register_data)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("signin"))

    context.update({
        "form": form,
    })

    return render_to_response('users/signup.html', context,
                              context_instance=RequestContext(request))


def signout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect(reverse("signin"))
