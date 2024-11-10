from rest_framework import serializers

from .models import AdminUser, AccessControl


class LoginSerializer(serializers.Serializer):
    email_id = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email_id')
        password = data.get('password')

        if email and password:
            try:
                user = AdminUser.objects.get(email_id=email)
                print(user)
                if user.check_password(password):
                    if not user.is_active:
                        raise serializers.ValidationError("Account is disabled.")
                    return user
                else:
                    raise serializers.ValidationError("Incorrect password.")
            except AdminUser.DoesNotExist:
                raise serializers.ValidationError("User does not exist.")
        else:
            raise serializers.ValidationError("Must include 'email_id' and 'password' fields.")
                

class LogoutSerializer(serializers.Serializer):
    pass


class AccessSerializer(serializers.ModelSerializer):
    user_admin = serializers.PrimaryKeyRelatedField(read_only=True)
    app_configuration = serializers.BooleanField(default=False)
    users = serializers.BooleanField(default=False)
    dashboard = serializers.BooleanField(default=False)
    reports = serializers.BooleanField(default=False)
    customer_support = serializers.BooleanField(default=False)
    admin_control = serializers.BooleanField(default=False)
    daitgpt = serializers.BooleanField(default=False)
    payment_gateway = serializers.BooleanField(default=False)
    onboarding = serializers.BooleanField(default=False)
    plan = serializers.BooleanField(default=False)
    policies = serializers.BooleanField(default=False)
    gender_and_sexuality = serializers.BooleanField(default=False)
    let_us_start = serializers.BooleanField(default=False)
    basic_details = serializers.BooleanField(default=False)
    interest = serializers.BooleanField(default=False)
    verification = serializers.BooleanField(default=False)
    export_data = serializers.BooleanField(default=False)
    add_user = serializers.BooleanField(default=False)
    edit_user = serializers.BooleanField(default=False)
    recycle_bin = serializers.BooleanField(default=False)
    refund = serializers.BooleanField(default=False)
    send_message = serializers.BooleanField(default=False)
    change_expiration_date = serializers.BooleanField(default=False)
    deactivate_account = serializers.BooleanField(default=False)
    add_note = serializers.BooleanField(default=False)
    delete_user = serializers.BooleanField(default=False)
    edit_report = serializers.BooleanField(default=False)
    view_attachment = serializers.BooleanField(default=False)
    view_profile = serializers.BooleanField(default=False)
    edit_support = serializers.BooleanField(default=False)
    add_new_admin = serializers.BooleanField(default=False)
    delete_admin = serializers.BooleanField(default=False)
    edit_admin = serializers.BooleanField(default=False)
    set_dait = serializers.BooleanField(default=False)
    upcoming_dait = serializers.BooleanField(default=False)
    setting = serializers.BooleanField(default=False)
    status = serializers.BooleanField(default=False)
    recycle_delete = serializers.BooleanField(default=False)
    recycle_recover = serializers.BooleanField(default=False)
    delete_report = serializers.BooleanField(default=False)
    delete_support = serializers.BooleanField(default=False)
    support = serializers.BooleanField(default=False)


    class Meta:
        model = AccessControl
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    access_control = AccessSerializer()

    class Meta:
        model = AdminUser
        exclude = ['email', 'groups', 'user_permissions']

    def create(self, validated_data):
        access_data = validated_data.pop('access_control')
        admin_user = AdminUser.objects.create(**validated_data)
        AccessControl.objects.create(user_admin=admin_user, **access_data)
        return admin_user
    

    def update(self, instance, validated_data):
        access_data = validated_data.pop('access_control', None) if 'access_control' in validated_data else None

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        if access_data:
            access_instance = instance.access
            for field, value in access_data.items():
                setattr(access_instance, field, value)
            access_instance.save()

        return instance
