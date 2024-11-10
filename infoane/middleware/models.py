from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser, Group, Permission


class AdminUser(AbstractUser):
    email_id = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='admin_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='admin_users')

    class Meta:
        db_table="access_control_adminuser"

    def save(self, *args, **kwargs):
        if not self.pk or self._password_changed():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _password_changed(self):
        if not self.pk:
            return True
        old_password = AdminUser.objects.get(pk=self.pk).password
        return old_password != self.password
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class AccessControl(models.Model):
    user_admin = models.ForeignKey(AdminUser, on_delete=models.CASCADE, related_name='access_control')
    dashboard = models.BooleanField(default=False)
    app_configuration = models.BooleanField(default=False)

    users = models.BooleanField(default=False)
    delete_user = models.BooleanField(default=False)
    add_user = models.BooleanField(default=False)
    edit_user = models.BooleanField(default=False)
    gender_and_sexuality = models.BooleanField(default=False)
    basic_details = models.BooleanField(default=False)
    interest = models.BooleanField(default=False)
    verification = models.BooleanField(default=False)
    export_data = models.BooleanField(default=False)

    customer_support = models.BooleanField(default=False)
    edit_support = models.BooleanField(default=False)
    delete_support = models.BooleanField(default=False)
    support = models.BooleanField(default=False)

    daitgpt = models.BooleanField(default=False)
    set_dait = models.BooleanField(default=False)
    upcoming_dait = models.BooleanField(default=False)

    payment_gateway = models.BooleanField(default=False)
    onboarding = models.BooleanField(default=False)
    plan = models.BooleanField(default=False)
    policies = models.BooleanField(default=False)
    let_us_start = models.BooleanField(default=False)
    
    refund = models.BooleanField(default=False)
    send_message = models.BooleanField(default=False)
    change_expiration_date = models.BooleanField(default=False)
    deactivate_account = models.BooleanField(default=False)
    add_note = models.BooleanField(default=False)

    edit_report = models.BooleanField(default=False)
    delete_report = models.BooleanField(default=False)
    reports = models.BooleanField(default=False)

    view_attachment = models.BooleanField(default=False)
    view_profile = models.BooleanField(default=False)

    admin_control = models.BooleanField(default=False)
    add_new_admin = models.BooleanField(default=False)
    delete_admin = models.BooleanField(default=False)
    edit_admin = models.BooleanField(default=False)

    setting = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    recycle_delete = models.BooleanField(default=False)
    recycle_recover = models.BooleanField(default=False)
    recycle_bin = models.BooleanField(default=False)
    

    def __str__(self):
        return f"AccessControl for {self.user_admin.email_id}"

    class Meta:
        verbose_name = "AccessControl"
        verbose_name_plural = "Access Control Permissions"

    class Meta:
        db_table = "access_control_accesscontrol"