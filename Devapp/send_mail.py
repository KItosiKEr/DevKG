# # from django.core.mail import EmailMessage

# # from django.conf import settings


# # def send_msg(email, type_work, company_name):
# #     mail = EmailMessage(
# #         f"Hi {company_name}",
# #         f"Success - {type_work}",
# #         settings.EMAIL_HOST_USER,
# #         [email]
# #     )
# #     mail.send()

# from django.core.mail import EmailMessage

# from django.conf import settings

# from Devapp.models import User


# # from django.contrib.auth import get_user_model

# # User = get_user_model()


# def send_msg_vacancy(type_work, salary, currency):
#     mail = EmailMessage(
#         f'Hi, new vacancy "{type_work}"',
#         f'Salary - {salary} {currency}',
#         settings.EMAIL_HOST_USER,
#         User.objects.values_list('email', flat=True)

#     )
#     mail.send()

# from celery import shared_task
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string


# @shared_task
# def send_mail_to_email(full_name, email, message, phone_number):
#     data = {
#         'full_name': full_name,
#         "email": email,
#         'message': message,
#         'phone_number': phone_number
#     }
#     html_body = render_to_string('h.html', data)
#     msg = EmailMultiAlternatives(subject='Здравствуйте', to=[email])
#     msg.attach_alternative(html_body, 'text/html')
#     msg.send()