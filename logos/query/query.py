from pydantic import BaseModel, Field, validator
from typing import Optional

class Query(BaseModel):
    """
    A class representing a user's query.

    Attributes:
        prompt (str): User inputted prompt.
        system_message (Optional[str]): System message to append to the user's prompt.
        schema (Optional[str]): Planning schema to decompose the user's prompt.
        
    """

    prompt: str = Field(..., description="User inputted prompt.")
    system_message: Optional[str] = Field(
        None,
        description="System message to append to the user's prompt."
    )
    schema: Optional[str] = Field(
        None,
        description="Planning schema to decompose the user's prompt."
    )
    schema_only: Optional[bool] = Field(
        False,
        description="Prompts LM to return the schema only."
    )
    validated_prompt: str = Field(None, description="For use by the LM.")

    @validator('prompt')
    def validate_prompt(cls, value):
        """
        Validate the prompt field.

        params:
            value: The prompt value to validate.
        return:
            The validated prompt value.
            
        raises:
            ValueError: If the prompt is less than 10 characters long.
            
        """
        if len(value) < 10:
            raise ValueError("Prompt should be at least 10 characters long")
        
        return value

    @validator('system_message')
    def validate_system_message(cls, value):
        """
        Validate the system_message field.

        params:
            value: The system_message value to validate.
        return:
            The validated system_message value.
        raises:
            ValueError: If the system_message is less than 10 characters long.
            
        """
        if value is not None and len(value) < 10:
            raise ValueError("System message should be at least 10 characters long")
        
        return value

    @validator('schema')
    def validate_schema(cls, value):
        """
        Validate the schema field.

        params:
            value: The schema value to validate.
        return:
            The validated schema value in uppercase.
        raises:
            ValueError: If the schema is not one of the allowed values (None, JSON, PDDL).
        
        """
        if value is not None and value.upper() not in ["JSON", "PDDL"]:
            raise ValueError("Schema should be one of: None, JSON, PDDL")
        
        return value.upper() if value is not None else None

    def __init__(self, **data):
        """
        Initialize the Query class.

        return:
            The structured text string.
        
        """
        super().__init__(**data)
        self.validated_prompt = self._validate_prompt()

    def _validate_prompt(self) -> str:
        """
        Create a structured text string combining the prompt, system_message, and schema.

        return:
            The structured text string.
        
        """
        validated_prompt = f"Prompt: {self.prompt}\n"
        
        if self.system_message:
            validated_prompt += f"System Message: {self.system_message}\n"

        if self.schema:
            validated_prompt += f"Create Schema to solve query in {self.schema}\n"
        
        if self.schema_only == True:
            validated_prompt += f"Return Schema Only\n"
            
        return validated_prompt