# from django.db.models.signals import post_save
# from Devapp.models import Vacancies
# from django.dispatch import receiver
# from Devapp.send_mail import send_msg_vacancy


# @receiver(post_save, sender=Vacancies)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         send_msg_vacancy(instance.type_work, instance.salary)