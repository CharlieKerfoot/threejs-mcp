# StackNode
Extends: EventDispatcher→Node→

Stack is a helper for Nodes that need to produce stack-based code instead of continuous flow.
They are usually needed in cases like If , Else .

## Constructor
`newStackNode( parent :StackNode)`
Constructs a new stack node.

## Properties
- `.isStackNode : boolean` — This flag can be used for type testing. Default is true .
- `.nodes : Array.<Node>` — List of nodes.
- `.outputNode :Node` — The output node. Default is null .
- `.parent :StackNode` — The parent stack node. Default is null .

## Methods
- `.Case( …params :any) :StackNode` — Represents a case statement in TSL. The TSL version accepts an arbitrary numbers of values.
The last parameter must be the callback method that should be executed in the true case.
- `.Default( method :function) :StackNode` — Represents the default code block of a Switch/Case statement.
- `.Else( method :function) :StackNode` — Represent an else statement in TSL.
- `.ElseIf( boolNode :Node, method :function) :StackNode` — Represent an elseif statement in TSL.
- `.If( boolNode :Node, method :function) :StackNode` — Represent an if statement in TSL.
- `.Switch( expression :any, method :function) :StackNode` — Represents a switch statement in TSL.
- `.addToStack( node :Node, index :number) :StackNode` — Adds a node to this stack.
- `.addToStackBefore( node :Node) :StackNode` — Adds a node to the stack before the current node.

## Source