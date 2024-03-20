"""
The seed class for the Logos library. All user queries begin with a decomposition
and comprehension phase.

A SCHEMA is highly encouraged as it provides the 'bumper lanes' for the user's
query to be processed by the langauge model (LM).

The 'game schema' for example instructs the LM to first intake the objective,
rules, and potential strategies for the game. This provides the scaffolding for
the LM to generate a more relevant response.

All queries will produce a state, action, and reward output. These elements are
passed to the 'reason' modules to step through a user's response using a specified
method or algorithm to decide on the best course of action based on score.

"""


from pydantic import BaseModel, Field
from typing import Optional


class QueryObeservation(BaseModel):
    user_query: str = Field(..., description="The user's query")
    instructions: str = Field(
        "Identify the main topic or intent of the user's query. \
        Provide a concise description of what the query is about \
        without attempting to answer the question itself.",
        const=True,
        description="Instructions for the LLM",
    )
    output_prefix: str = Field(
        "Topic/Intent:",
        const=True,
        description="Output prefix for the LLM's response"
    )

    def to_prompt(self) -> str:
        return f"User query: {self.user_query}\n\nInstructions: {self.instructions}\n\n{self.output_prefix}"

    
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


class Schema(BaseModel):
    system: str = Field(default="You are a helpful AI assistant.")
    input: int = Field(...)
    output: int = Field(...)


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