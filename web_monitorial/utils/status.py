# Copied from https://github.com/encode/django-rest-framework/blob/master/rest_framework/status.py

"""
Descriptive HTTP status codes, for code readability.
See RFC 2616 - https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
And RFC 6585 - https://tools.ietf.org/html/rfc6585
And RFC 4918 - https://tools.ietf.org/html/rfc4918
"""


def is_informational(code) -> bool:
    return 100 <= code <= 199


def is_success(code) -> bool:
    return 200 <= code <= 299


def is_redirect(code) -> bool:
    return 300 <= code <= 399


def is_client_error(code) -> bool:
    return 400 <= code <= 499


def is_server_error(code) -> bool:
    return 500 <= code <= 599

status_codes = {
    "http_100_continue": 100,
    "http_102_processing": 102,
    "http_103_early_hints":103,
    "http_200_ok":200,
    "http_201_created":201,
    "http_202_accepted":202,
    "http_203_non_authoritative_information":203,
    "http_204_no_content":204,
    "http_205_reset_content":205,
    "http_206_partial_content":206,
    "http_207_multi_status":207,
    "http_208_already_reported":208,
    "http_226_im_used":226,
    "http_300_multiple_choices":300,
    "http_301_moved_permanently":301,
    "http_302_found":302,
    "http_303_see_other":303,
    "http_304_not_modified":304,
    "http_305_use_proxy":305,
    "http_306_reserved":306,
    "http_307_temporary_redirect":307,
    "http_308_permanent_redirect":308,
    "http_400_bad_request":400,
    "http_401_unauthorized":401,
    "http_402_payment_required":402,
    "http_403_forbidden":403,
    "http_404_not_found":404,
    "http_405_method_not_allowd":405,
    "http_406_not_acceptable":406,
    "http_407_proxy_authentication_required":407,
    "http_408_request_timeout":408,
    "http_409_conflict":409,
    "http_410_gone":410,
    "http_411_length_required":411,
    "http_412_precondition_failed":412,
    "http_413_request_entity_too_large":413,
    "http_414_request_uri_too_long":414,
    "http_415_unsupported_media_type":415,
    "http_416_request_range_not_satisfiable":416,
    "http_417_expectation_failed":417,
    "http_418_im_a_teapot":418,
    "http_421_missdirected_request":421,
    "http_422_unprocessable_entity":422,
    "http_423_locked":423,
    "http_424_failed_dependency":424,
    "http_425_too_early":425,
    "http_426_upgrade_required":426,
    "http_428_precondition_required":428,
    "http_429_too_mant_requests":429,
    "http_431_request_header_fields_too_large":431,
    "http_451_unavailable_for_legal_reasons":451,
    "http_500_internal_server_error":500,
    "http_501_not_implemented":501,
    "http_502_bad_gateway":502,
    "http_503_service_unavailable":503,
    "http_504_gateway_timeout":504,
    "http_505_http_version_not_supported":505,
    "http_506_variant_also_negotiates":506,
    "http_507_insufficient_storage":507,
    "http_508_loop_detected":508,
    "http_509_banwith_limit_exceeded":509,
    "http_510_not_extended":510,
    "http_511_network_authentication_required":511,
}
