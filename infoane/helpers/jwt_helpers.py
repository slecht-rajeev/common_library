from datetime import datetime, timedelta
import jwt
from logging import getLogger
logger = getLogger("django")
class JWTComponent:
    def __init__(self, algorithm = "RS256"):
        self.algorithm = algorithm

    def encode_jwt(self, key, payload):
        return jwt.encode(payload, key, algorithm=self.algorithm)

    def decode_jwt(self, key, payload):
        return jwt.decode(payload, key, algorithms=[self.algorithm])

    
    def validate_token(self, key, token):
        try:
            # Decode and verify the token
            # decoded_token = jwt.decode(token, PUBLIC_KEY, algorithms=['RS256'])
            decoded_token = self.decode_jwt(key, token)

            
            # Perform additional validation if needed
            # For example, check if the token has not expired
            current_time = datetime.utcnow()
            if 'exp' in decoded_token and datetime.utcfromtimestamp(decoded_token['exp']) < current_time:
                logger.debug("Token has expired")
                return False
            # Additional validation checks can be added here
            # If all checks pass, the token is valid
            return decoded_token

        except jwt.ExpiredSignatureError:
            logger.debug("Token has expired")
            return False
        except jwt.InvalidTokenError:
            logger.debug("Invalid token")
            return False



    


    