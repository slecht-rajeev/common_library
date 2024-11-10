import logging
from functools import wraps
from django.http import JsonResponse
import jwt
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def check_access_token(view_func):
    @wraps(view_func)
    def _wrapped_view(*args, **kwargs):
        if len(args) > 1 and hasattr(args[1], 'META'):
            # For class-based views (CBVs)
            request = args[1]
        else:
            # For function-based views (FBVs)
            request = args[0]

        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header or not auth_header.startswith('Bearer '):
            logger.warning("Authorization header not provided. Bypassing permission check.")
            return view_func(*args, **kwargs)
            # return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)
        
        token = auth_header.split(' ')[1]

        try:
            # Decode the token without verifying the signature
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            exp_timestamp = decoded_token.get('exp')
            if exp_timestamp:
                current_timestamp = datetime.now(timezone.utc).timestamp()
                if current_timestamp > exp_timestamp:
                    return JsonResponse({'error': 'Token has expired'}, status=401)
            request.user = decoded_token  # Optionally, you can add the decoded token to the request

        except jwt.DecodeError as e:
            return JsonResponse({'error': 'Invalid token format', 'details': str(e)}, status=401)
        except jwt.InvalidTokenError as e:
            return JsonResponse({'error': 'Invalid token', 'details': str(e)}, status=401)
        except Exception as e:
            return JsonResponse({'error': 'Token is not valid', 'details': str(e)}, status=401)
        
        return view_func(*args, **kwargs)

    return _wrapped_view
