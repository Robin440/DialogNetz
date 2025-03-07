from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

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
        from_email = EMAIL_HOST_USER
        recipient_list = [email]

        context = {
            'invitation_code': invitation_code,
            'otp': otp,
        }
        html_content = render_to_string('invitation.html', context)
        text_content = f"""
Hello,

You have been invited to join DialogNetz, the premier platform for seamless communication within your organization.

To get started, please click on the following link or use the OTP provided below:

Invitation Link: https://dailognetz.com/invite?code={invitation_code}
Your OTP: {otp}

We look forward to seeing you on DialogNetz!

Best regards,
The DialogNetz Team
"""

        # Create the email
        email_message = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()

    except Exception as e:
        print(f"_____________________error_____________{e}________________________________________________")
        return False

    return True



def send_self_registration_verification(request):
    """
    Send a test email to the email address specified in the settings file.
    """
    otp=request.data.get('otp')
    email = request.data.get("email")
    invitation_code = request.data.get("invitation_code")
    try:
        subject = 'Welcome to DialogNetz! Complete Your Registration Today'
        from_email = EMAIL_HOST_USER
        recipient_list = [email]

        context = {
            'invitation_code': invitation_code,
            'otp': otp,
        }
        html_content = render_to_string('self_registration.html', context)
        text_content = f"""
Hello,

Welcome to DialogNetz, your go-to platform for seamless communication within your organization.

To begin, please click on the link below or use the OTP provided to complete your registration:

Registration Link: https://dailognetz.com/register?code={invitation_code}
Your OTP: {otp}

We're excited to have you join us on DialogNetz!

Best regards,
The DialogNetz Team

"""
        email_message = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()
    except Exception as e:
        print(f"_____________________error_____________{e}________________________________________________")
        return False
    return True

        
