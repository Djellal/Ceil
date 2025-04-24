from django.db import models
from django.utils.translation import gettext_lazy as _

class Session(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Session Code")
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("Session Name")
    )
    name_ar = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("Arabic Session Name")
    )
    start_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("Start Date")
    )
    end_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("End Date")
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")


class AppSettings(models.Model):
    organization_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Ceilgest',
        verbose_name=_("Organization Name")
    )
    organization_logo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Organization Logo")
    )  # Path to image file
    address = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Address")
    )
    tel = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_("Telephone")
    )
    email = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Email")
    )
    website = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Website")
    )
    facebook = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Facebook")
    )
    twitter = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Twitter")
    )
    linkedin = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("LinkedIn")
    )
    youtube = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("YouTube")
    )
    current_session = models.ForeignKey(
        Session,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='app_settings',
        verbose_name=_("Current Session")
    )
    registration_opened = models.BooleanField(
        default=False,
        verbose_name=_("Registration Opened")
    )
    terms_and_conditions = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Terms and Conditions")
    )

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = _("Application Settings")
        verbose_name_plural = _("Application Settings")


    @classmethod
    def get_settings(cls):
        """
        Returns the singleton AppSettings instance.
        If no instance exists, creates one with default values.
        """
        settings, created = cls.objects.get_or_create(
            defaults={
                'organization_name': 'Ceil UFAS1',
                'organization_logo': 'path/to/default/logo.png',
                'address': '123 Main St, City, Country',
                'tel': '+1234567890',
                'email': 'ceil@univ-setif.dz',
            }
        )
        return settings
