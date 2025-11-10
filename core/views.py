from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.
def main(request):
    return render(request, "main/main.html" )

def login_view(request):
    return render(request, "login2.html" )


def signup(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['signup-password']
        pass2 = request.POST['signup-confirm-password']

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists. Try other email")
            return redirect('login')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('login')



        
        

        myuser = User.objects.create_user(email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Account successfully created.")


        #Welcome email
        # subject = "Welcome to SOS Pay!"
        # message = "Hello " + myuser.first_name + "!!\n" + "Welcome to SOS Pay\n Thank You for visiting this site.\n We have sent you a confirmation email. Please confirm your email address to activate your account. \n\n  Thank you "+fname
        # from_email = 'larteyian@gmail.com'
        # receipient_list = [myuser.email]
        # send_mail(subject, message, from_email, receipient_list, fail_silently=False)



        return redirect('signin')
    
    return redirect('login_view')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('core-main')

def signin(request):
    if request.method == "POST":
        email = request.POST['login-email']
        pass1 = request.POST['login-password']

        user = authenticate(email=email, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('main')  # Redirect to dashboard or main page
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return redirect('core-main')




# if user is not None:
#             user_id = user.id
            
#             # return render(request, "authentication/index.html", {'fname': fname})
#             if user.last_login == None:
#                 # login(request, user)
#                 return redirect(f'/login/multi/{user_id}/')
#             else:
#                 # request.session['user_email']= email
                
#                 # return redirect('otp')
#                 # send_otp(request)
#                 email_otp= send_otp(request)
#                 subject = "Email Verification!"
#                 message = "Hello " + user.first_name +  "!!\n" + "Welcome to SOS Pay\n Thank You for visiting this site.\n Below is the otp to complete your login. Please type in this otp in the website to login:\n" +email_otp
#                 from_email = 'larteyian@gmail.com'
#                 receipient_list = [user.email]
#                 send_mail(subject, message, from_email, receipient_list, fail_silently=False)
#                 request.session['email']=user.email
#                 return redirect('otp')