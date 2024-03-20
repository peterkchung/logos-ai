from pydantic import BaseModel, Field
from typing import Optional

import logging
import os

class Query(BaseModel):
    """
    Query from user.
    
    Attributes:
        query (str): Query provided by user.
    
    Functions:

    """
    query: str = Field(
        ...,
        description="Query provided by user."
    )