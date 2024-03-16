"""
Schema

"""


from pydantic import BaseModel, Field
from typing import Optional


class SchemaField(Field):
    def __init__(self, *args, field_type, **kwargs):
        self.field_type = field_type
        super().__init__(*args, **kwargs)

def SystemField(*args, **kwargs):
    return SchemaField(*args, field_type="system", **kwargs)

def InputField(*args, **kwargs):
    return SchemaField(*args, field_type="input", **kwargs)

def OutputField(*args, **kwargs):
    return SchemaField(*args, field_type="output", **kwargs)


class SchemaMeta(type(BaseModel)):
    def __new__(mcs, name, bases, namespace, **kwargs):
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, SchemaField):
                fields[key] = (value.type_, value)
        namespace.update(fields)
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        return cls


class Schema(BaseModel, metaclass=SchemaMeta):
    @classmethod
    def get_fields_by_type(cls, field_type):
        return {k: v for k, v in cls.__fields__.items() if isinstance(v, SchemaField) and v.field_type == field_type}

    @property
    def system_fields(self):
        return self.get_fields_by_type("system")

    @property
    def input_fields(self):
        return self.get_fields_by_type("input")

    @property
    def output_fields(self):
        return self.get_fields_by_type("output")


def make_schema(name: str, fields: dict) -> Type[Schema]:
    return create_model(name, __base__=Schema, **fields)