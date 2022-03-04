from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from .models import transactions


# Create your views here.
@login_required
def sendemail(request):
    if request.method == "POST":
        # getting inputs to variables
        fto = request.POST.get('email')
        famount = request.POST.get('amount')
        fname = request.POST.get('name')

        # saving into database transactions table
        transaction = transactions(toemail=fto, toname=fname, amount=famount)
        transaction.save()

        # create url
        content = """
        You Have a New Transaction
        Confirm Your Payment
        Link: http://127.0.0.1:8000
        """

        # sending message as an email
        send_mail(
            # subject
            "Transfer Money",
            # message
            content,
            # from email
            settings.EMAIL_HOST_USER,
            # rec list
            [fto]
        )
        return render(request, 'email.html', {'title': 'New Transactions'})
    else:
        return render(request, 'email.html', {'title': 'New Transactions'})


# dashboard that displays not confirmed transactions
@login_required
def home(request):
    useremail = request.user.email
    unmarked = transactions.objects.filter(toemail=useremail, status=0)
    return render(request, 'home.html', {'unmarked': unmarked})


# new user registration form
# once you signed up, system redirects to login page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


# this updates the status of transactions as viewed and confirmed
# redirect to home once updated
@login_required
def update(request, id):
    # update status to 1
    trans = transactions.objects.get(id=id)
    trans.status = 1
    trans.save()
    return redirect('home')