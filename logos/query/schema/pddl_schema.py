"""
Example:
    generator = PDDLGenerator()

    types = ["type1", "type2"]
    predicates = ["(predicate1 ?x - type1 ?y - type2)", "(predicate2 ?x - type1)"]
    actions = [
        ("action1", [("x", "type1"), ("y", "type2")], ["(predicate1 ?x ?y)"], ["(predicate2 ?x)"]),
        ("action2", [("x", "type1")], ["(predicate2 ?x)"], ["(not (predicate2 ?x))"])
    ]

    domain_str = generator.generate_domain("my_domain", types, predicates, actions)
    print(domain_str)

    objects = [("obj1", "type1"), ("obj2", "type2")]
    init = ["(predicate1 obj1 obj2)"]
    goal = ["(predicate2 obj1)"]

    problem_str = generator.generate_problem("my_problem", "my_domain", objects, init, goal)
    print(problem_str)

"""

class PDDLGenerator:
    """
    A class for generating PDDL (Planning Domain Definition Language) definitions and schemas.

    Methods:
        generate_domain(domain_name, types, predicates, actions):
            Generates a PDDL domain definition string based on the provided information.

        generate_problem(problem_name, domain_name, objects, init, goal):
            Generates a PDDL problem definition string based on the provided information.

    Helpers:
        _generate_action(action):
            Generates the PDDL representation of an action.
    
    """

    def generate_domain(self, domain_name, types, predicates, actions):
        """
        Generates a PDDL domain definition string.

        Args:
            domain_name (str): The name of the planning domain.
            types (list): A list of strings representing the types of objects in the domain.
            predicates (list): A list of strings representing the predicates in the domain.
            actions (list): A list of tuples representing the actions in the domain.
                Each action tuple should have the following format:
                (name, parameters, preconditions, effects)
                - name (str): The name of the action.
                - parameters (list): A list of tuples representing the parameters of the action.
                    Each parameter tuple should have the format: (name, type)
                - preconditions (list): A list of strings representing the preconditions of the action.
                - effects (list): A list of strings representing the effects of the action.

        Returns:
            str: The generated PDDL domain definition string.
        """
        domain = f"(define (domain {domain_name})\n"
        domain += "  (:requirements :strips :typing)\n"
        domain += "  (:types\n"

        for type_ in types:
            domain += f"    {type_}\n"
        domain += "  )\n\n"
        domain += "  (:predicates\n"

        for predicate in predicates:
            domain += f"    ({predicate})\n"
        domain += "  )\n\n"

        for action in actions:
            domain += self._generate_action(action)
        domain += ")\n"

        return domain


    def _generate_action(self, action):
        """
        Generates the PDDL representation of an action.

        Args:
            action (tuple): A tuple representing an action, with the following format:
                (name, parameters, preconditions, effects)
                - name (str): The name of the action.
                - parameters (list): A list of tuples representing the parameters of the action.
                    Each parameter tuple should have the format: (name, type)
                - preconditions (list): A list of strings representing the preconditions of the action.
                - effects (list): A list of strings representing the effects of the action.

        Returns:
            str: The PDDL representation of the action.
        
        """
        
        name, parameters, preconditions, effects = action
        
        action_str = f"  (:action {name}\n"
        action_str += "    :parameters ("
        
        for param in parameters:
            action_str += f" ?{param[0]} - {param[1]}"
        
        action_str += ")\n"
        action_str += "    :precondition (and\n"
        
        for precond in preconditions:
            action_str += f"      ({precond})\n"
        
        action_str += "    )\n"
        action_str += "    :effect (and\n"
        
        for effect in effects:
            action_str += f"      ({effect})\n"
        
        action_str += "    )\n"
        action_str += "  )\n\n"
        
        return action_str


    def generate_problem(self, problem_name, domain_name, objects, init, goal):
        """
        Generates a PDDL problem definition string.

        Args:
            problem_name (str): The name of the planning problem.
            domain_name (str): The name of the planning domain.
            objects (list): A list of tuples representing the objects in the problem.
                Each object tuple should have the format: (name, type)
            init (list): A list of strings representing the initial state of the problem.
            goal (list): A list of strings representing the goal state of the problem.

        Returns:
            str: The generated PDDL problem definition string.
        
        """
        
        problem = f"(define (problem {problem_name})\n"
        problem += f"  (:domain {domain_name})\n"
        problem += "  (:objects\n"
        
        for obj in objects:
            problem += f"    {obj[0]} - {obj[1]}\n"
        
        problem += "  )\n\n"
        problem += "  (:init\n"
        
        for init_pred in init:
            problem += f"    ({init_pred})\n"
        
        problem += "  )\n\n"
        problem += "  (:goal\n"
        problem += "    (and\n"
        
        for goal_pred in goal:
            problem += f"      ({goal_pred})\n"
        
        problem += "    )\n"
        problem += "  )\n"
        problem += ")\n"
        
        return problem