from marshmallow import Schema, fields


class TaskSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    repeat = fields.Str()
    all_day = fields.Bool()
    start = fields.DateTime(required=True)
    end = fields.DateTime()
