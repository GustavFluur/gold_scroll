from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    
    scroll_user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    main_insert_country = CountryField(blank_label='Country *', null=True, blank=True)
    main_insert_zip_code = models.CharField(max_length=20, null=True, blank=True)
    main_insert_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    main_insert_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    main_insert_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    main_insert_county = models.CharField(max_length=80, null=True, blank=True)
    main_insert_gender = models.CharField(max_length=80, null=True, blank=True)
    main_insert_date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_scroll_user_profile(sender, instance, created, **kwargs):

    if created:
        UserAccount.objects.create(user=instance)
    # Existing users: just save the profile
    instance.useraccount.save()