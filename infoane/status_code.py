from infoane import Service
from infoane.consts import STATUS_CODE, MESSAGE, SUCCESS_CODE, FAILURE_CODE

success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}
generic_error_1 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Please try again after sometime"}
not_valid_access_token = {STATUS_CODE: FAILURE_CODE, MESSAGE: "You are not allowed to update the data"}
object_not_found = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Data not found"}


def invalide_value_not_allowed(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f"Invalid value allowed in {field_name}",
    }

# make error code in asc order
def field_required_error(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{field_name} is mandatory',
    }


def field_should_be_boolean_type(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{field_name} should be boolean type',
    }


def field_should_be_string_type(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{field_name} should be string type',
    }


def field_should_be_int_type(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{field_name} should be int type',
    }


def table_not_exist(table_name, id):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{table_name} having id - {id} does not exist',
    }


def error_while_log_table_saving(table_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'Error while saving log table for {table_name}',
    }


def field_cannot_be_blank(field_name):
    return {
        'status_code': FAILURE_CODE,
        'message': f'{field_name} cannot be blank',
    }


def field_should_be_list_type(field_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'{field_name} should be list type',
    }


def field_list_cannot_be_empty(self):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f"{self} cannot be empty.",
    }


def api_call_failed(api_url, message):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f"{api_url} call failed - {message}"
    }


def method_not_allowed(method):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f"{method} method not allowed"
    }


def invalide_value_not_allowed(field_name):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f"Invalid value allowed in {field_name}"
    }


def negative_value_not_allowed(field_name):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f"{field_name} cannot be negative"
    }


def wrong_decimal_precision(field_name, decimal_precision):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f"{field_name} cannot have more than {decimal_precision} decimal"
    }

def service_api_failed_because(service_name,reason):
    return {
        STATUS_CODE: FAILURE_CODE, 
        MESSAGE: f'{service_name} API Failed becasue : {reason}'
    }



def invalid_log_model(table_name):
    return {
        STATUS_CODE: FAILURE_CODE,
        MESSAGE: f'Invalid log model initialized for model {table_name}',
    }
