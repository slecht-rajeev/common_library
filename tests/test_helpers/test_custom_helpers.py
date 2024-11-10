from infoane import Service
Service(code=1)
from infoane.helpers.custom_helpers import get_response
import logging
# from infoane.consts import DATE_YYYY_MM_DD

logger = logging.getLogger(__name__)


class TestCustomHelpers:

    def test_get_response_without_data(self):
        status_attribute = {"status_code":1000, "message":"test"}
        actual_response = get_response(status_attribute=status_attribute)
        expected_response = {'status': status_attribute['status_code'], 'message': status_attribute['message']}
        assert actual_response == expected_response