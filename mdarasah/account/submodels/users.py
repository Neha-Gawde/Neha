from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_admin = models. BooleanField(default=False)
    is_subadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    created_at = models.BooleanField(default=False)
    updated_at = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # permissions = [
        #     ("view_all_users", "Can view all users"),
        #     ("change_all_users", "Can change all users"),
        #     ("add_all_user", "Can change all users"),
        #     ("remove_all_users", "Can change all users"),

        #     ("view_all_teachers", "Can view all teachers"),
        #     ("change_all_teachers", "Can change all teachers"),
        #     ("add_all_teachers", "Can change all teachers"),
        #     ("remove_all_teachers", "Can change all teachers"),
            
        #     ("view_all_students", "Can view all students"),
        #     ("change_all_students", "Can change all students"),
        #     ("add_all_students", "Can change all students"),
        #     ("remove_all_students", "Can change all tudents"),


        # ]

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
