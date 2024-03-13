import os
from huggingface_hub import InferenceClient

"""
This file contains the base classes for creating agents in the IntelliAgent framework.

- Step: Represents a step in the agent's workflow, such as a thought, an action, or an output.
- Agent: Represents an object bound to a language model (LLM) and optional tools to execute tasks.

"""

class Step:
    
    """
    'Step' class is an object representing a step in the agent's workflow.

    The step could be a thought, an action, or an output.
    
    Steps are logged to console for debugging and reporting.
    
    """

    def __init__(self, **kwargs):
        self


class Agent:
    
    """
    'Agent' class creates an object representing an agent, which represents a LLM equipped with
    a ReAct/COT prompt and optionally tools to execute on tasks.

    Agents generate steps.

    Each step represents a thought, an action, or an output.
    
    """

    def __init__(self, model, prompt, tools, memory, **kwargs):
        self.model = model
        self.prompt = prompt
        self.tools = tools
        self.memory = memory
        self.scratpad = None

    def _create_step(self, input):
        
        """
        Create a step based on the evaluated query.

        Args:
            query (str): The query to be evaluated.

        Returns:
            Step: The created step object.
        
        """
        
        """
        psuedocode:
        
        if not scratpad:
            query input
            log query
            evaluate query
            log evaluation
            generate next step
            log next step
            take action
            log action decided
            output provided
            log output provided
            evaluate output
            log evaluation
            generate next step
            ...
            if next step == Final | max_steps:
                return final
        
        """
        
        return None
    
    
    def _evaluate(self, query):
        
        """
        Evaluate the step to determine the next step for the agent.

        Args:
            query (str): The query to be evaluated.

        Returns:
            str: The assigned task based on the evaluation of the query.
        
        """
        
        """
        psuedocode: 
        
        if query:
            _create_step
        
        """
        return None

    
    def _use_tool(self, query, tool):
        
        """
        Use a tool based on the evaluated query.

        Args:
            query (str): The query to be evaluated.
            tool (Tool): The tool to be used.

        Returns:
            function: The execute function of the tool if the evaluation matches the tool's description, otherwise None.
        
        """
        eval = self._evaluate_query(query)
        
        if eval == tool.description:
            return tool.execute
        else:
            pass
            
        return None