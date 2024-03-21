from pydantic import BaseModel, Field, validator
from typing import Optional, List

from logos import Query


class PDDLProblem(BaseModel):
    """
    A class representing a PDDL problem.

    Attributes:
        domain (str): The domain name of the PDDL problem.
        objects (List[str]): The list of objects in the PDDL problem.
        init (List[str]): The initial state of the PDDL problem.
        goal (str): The goal state of the PDDL problem.
        
    """

    domain: str = Field(..., description="The domain name of the PDDL problem.")
    objects: List[str] = Field(..., description="The list of objects in the PDDL problem.")
    init: List[str] = Field(..., description="The initial state of the PDDL problem.")
    goal: str = Field(..., description="The goal state of the PDDL problem.")


class Step(BaseModel):
    """
    A class representing a step in the plan.

    Attributes:
        action (str): The action to be performed in the step.
        description (Optional[str]): The optional description of the step.
        
    """

    action: str = Field(..., description="The action to be performed in the step.")
    description: Optional[str] = Field(None, description="The optional description of the step.")


class Proposal(BaseModel):
    """
    A class representing a proposal for solving a PDDL problem.

    Attributes:
        problem (PDDLProblem): The PDDL problem to be solved.
        steps (List[Step]): The list of steps in the proposed plan.
        
    """

    problem: PDDLProblem = Field(..., description="The PDDL problem to be solved.")
    steps: List[Step] = Field([], description="The list of steps in the proposed plan.")

    @validator('steps')
    def validate_steps(cls, value):
        """
        Validate the steps field.

        params: 
            value: The steps value to validate.
        return:
            The validated steps value.
        raises
            ValueError: If the steps list is empty.
            
        """
        if not value:
            raise ValueError("At least one step must be provided in the proposal.")
        
        return value


def generate_proposal_prompt(proposal: Proposal) -> str:
    """
    Generate a structured prompt for proposing steps to solve a PDDL problem.

    params:
        proposal: The proposal containing the PDDL problem and steps.
    return:
        The generated prompt string.
    
    """
    problem = proposal.problem
    steps = proposal.steps

    prompt = f"PDDL Problem:\n"
    prompt += f"Domain: {problem.domain}\n"
    prompt += f"Objects: {', '.join(problem.objects)}\n"
    prompt += f"Initial State:\n"
    
    for state in problem.init:
        prompt += f"  {state}\n"
    
    prompt += f"Goal State: {problem.goal}\n\n"

    prompt += f"Proposed Steps:\n"
    
    for i, step in enumerate(steps, start=1):
        prompt += f"Step {i}: {step.action}\n"
        if step.description:
            prompt += f"  Description: {step.description}\n"

    prompt += f"\nPropose the next step to reach the goal state."

    return prompt