# RoundedBoxGeometry
Extends: EventDispatcher→BufferGeometry→BoxGeometry→

A special type of box geometry with rounded corners and edges.

## Constructor
`newRoundedBoxGeometry( width :number, height :number, depth :number, segments :number, radius :number)`
Constructs a new rounded box geometry.

## Import

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :RoundedBoxGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source