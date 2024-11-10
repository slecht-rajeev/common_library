import logging
from functools import wraps
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import AdminUser, AccessControl

logger = logging.getLogger(__name__)


def check_users_permission(permission_name: str):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(*args, **kwargs):

            if len(args) > 1:
                # Class-based view
                view_instance, request = args[0], args[1]
            else:
                # Function-based view
                view_instance, request = None, args[0]
            
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                logger.warning("Authorization header not provided. Bypassing permission check.")
                return view_func(view_instance, request, *args[2:], **kwargs) if view_instance else view_func(request, *args[1:], **kwargs)
            
            user = request.user
            if not user.is_authenticated:
                logger.error(f"User not authenticated")
                return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                access_control = get_object_or_404(AccessControl, user_admin=user)
                if not getattr(access_control, permission_name, False):
                    logger.error(f"Access control not defined for {permission_name}")
                    return Response({"error": f"Permission denied: 'Permission {permission_name}' required"}, status=status.HTTP_403_FORBIDDEN)
                
            except AdminUser.DoesNotExist:
                logger.error(f"Access control not found")
                return Response({"error": "User access control not found"}, status=status.HTTP_404_NOT_FOUND)

            if view_instance:
                return view_func(view_instance, request, *args[2:], **kwargs)
            else:
                return view_func(request, *args[1:], **kwargs)

        return wrapped_view

    return decorator
