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
    organization_logo = models.ImageField(
        upload_to='logos/',
        null=True,
        blank=True,
        verbose_name=_("Organization Logo")
    )  # Changed from CharField to ImageField
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


class State(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("State Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic State Name")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")


class Municipality(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Municipality Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic Municipality Name")
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='municipalities',
        verbose_name=_("State")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Municipality")
        verbose_name_plural = _("Municipalities")


class Profession(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Profession Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic Profession Name")
    )
    fee_value = models.FloatField(
        null=False,
        blank=False,
        verbose_name=_("Fee Value")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")


class CourseType(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Course Type Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic Course Type Name")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Course Type")
        verbose_name_plural = _("Course Types")


class Course(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Course Code")
    )
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Course Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic Course Name")
    )
    duration = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_("Duration (hours)")
    )
    image = models.ImageField(
        upload_to='courses/',
        null=True,
        blank=True,
        verbose_name=_("Course Image")
    )
    course_type = models.ForeignKey(
        CourseType,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name=_("Course Type")
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name=_("Is Active")
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")


class CourseLevel(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Level Name")
    )
    name_ar = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_("Arabic Level Name")
    )
    duration = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_("Duration (hours)")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='levels',
        verbose_name=_("Course")
    )
    next_level = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='previous_levels',
        verbose_name=_("Next Level")
    )

    def __str__(self):
        return f"{self.course.code} - {self.name}"

    class Meta:
        verbose_name = _("Course Level")
        verbose_name_plural = _("Course Levels")
