from marshmallow import Schema, fields

class TaskSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    repeat = fields.Str()
    all_day = fields.Bool()
    start = fields.DateTime()
    end = fields.DateTime()