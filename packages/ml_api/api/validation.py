import typing as t
from marshmallow import Schema, fields
from marshmallow import ValidationError


class DanoneWaterRequestSchema(Schema):
    Alley = fields.Str(allow_none=True)
    BedroomAbvGr = fields.Integer()
    BsmtCond = fields.Str()
    BsmtFinSF2 = fields.Float()

def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    """Remove input data rows with errors."""
    indexes = errors.keys()
    # delete them in reverse order so that you don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input

def validate_inputs(input_data):
    """Check prediction inputs against schema."""
    # set many=True to allow passing in a list
    schema = DanoneWaterRequestSchema(strict=True, many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors


