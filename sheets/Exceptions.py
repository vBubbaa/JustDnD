from rest_framework.exceptions import APIException


class CharacterSheetLimitExceeded(APIException):
    status_code = 400
    default_detail = 'Character sheet limit exceeded.'
    default_code = 'Limit Exceeded'


class TemplateLimitExceeded(APIException):
    status_code = 400
    default_detail = 'Template limit exceeded.'
    default_code = 'Limit Exceeded'
