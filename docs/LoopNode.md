# LoopNode
Extends: EventDispatcher→Node→

This module offers a variety of ways to implement loops in TSL. In it's basic form it's: However, it is also possible to define a start and end ranges, data types and loop conditions: Loop( { start: int( 0 ), end: int( 10 ), type: 'int', condition: '<' }, ( { i } ) => {
} ); Nested loops can be defined in a compacted form: Loop( 10, 5, ( { i, j } ) => {
} ); Loops that should run backwards can be defined like so: Loop( { start: 10 }, () => {} ); It is possible to execute with boolean values, similar to the while syntax. const value = float( 0 ).toVar();
Loop( value.lessThan( 10 ), () => {
	value.addAssign( 1 );
} ); The module also provides Break() and Continue() TSL expression for loop control.

## Constructor
`newLoopNode( params :Array.<any>)`
Constructs a new loop node.

## Methods
- `.getProperties( builder :NodeBuilder) : Object` — Returns properties about this node.
- `.getVarName( index :number) : string` — Returns a loop variable name based on an index. The pattern is 0 = i , 1 = j , 2 = k and so on.

## Source