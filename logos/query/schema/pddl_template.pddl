(define (domain <domain_name>)
  (:requirements :strips :typing)
  (:types
    ; Define the types of objects in the domain
    <type1> <type2> ...
  )

  (:predicates
    ; Define the predicates in the domain
    (<predicate1> ?<param1> - <type1> ?<param2> - <type2> ...)
    (<predicate2> ?<param1> - <type1> ?<param2> - <type2> ...)
    ...
  )

  (:action <action_name>
    :parameters (?<param1> - <type1> ?<param2> - <type2> ...)
    :precondition (and
      ; Define the preconditions for the action
      (<predicate1> ?<param1> ?<param2>)
      (<predicate2> ?<param1> ?<param2>)
      ...
    )
    :effect (and
      ; Define the effects of the action
      (not (<predicate1> ?<param1> ?<param2>))
      (<predicate3> ?<param1> ?<param2>)
      ...
    )
  )

  ; Define additional actions as needed
  (:action <action_name>
    ...
  )
)

(define (problem <problem_name>)
  (:domain <domain_name>)
  (:objects
    ; Define the objects in the problem instance
    <obj1> - <type1>
    <obj2> - <type2>
    ...
  )

  (:init
    ; Define the initial state of the problem
    (<predicate1> <obj1> <obj2>)
    (<predicate2> <obj1> <obj2>)
    ...
  )

  (:goal
    ; Define the goal state of the problem
    (and
      (<predicate3> <obj1> <obj2>)
      (<predicate4> <obj1> <obj2>)
      ...
    )
  )
)