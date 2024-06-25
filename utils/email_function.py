# views.py
from django.core.mail import send_mail
from django.http import HttpResponse
from core.settings import EMAIL_HOST_USER
EMAIL_HOST_USER = EMAIL_HOST_USER


def send_invitation_email(request):
    """
    Send a test email to the email address specified in the settings file.
    """
    print(f"++++++++++++++++++++++++ {EMAIL_HOST_USER} ++++++++++++++++++++++++++++++++++++++")
    otp = request.data.get('otp')
    invitation_code = request.data.get("invitation_code")
    email = request.data.get("email")

    print(f"----------------------- {email} ----------------------------------------")
    try:
        subject = 'Invitation from DialogNetz'
        message = f'''
Hello,

You have been invited to join DialogNetz, the premier platform for seamless communication within your organization.

To get started, please click on the following link or use the OTP provided below:

Invitation Link: https://dailognetz.com/invite?code={invitation_code}
Your OTP: {otp}

We look forward to seeing you on DialogNetz!

Best regards,
The DialogNetz Team
'''
        from_email = EMAIL_HOST_USER
        recipient_list = [email]
        
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"__________________________________{e}________________________________________________")
        return False
    
    return True
