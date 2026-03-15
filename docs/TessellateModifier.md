# TessellateModifier

This class can be used to modify a geometry by breaking its edges if they
are longer than maximum length.

## Constructor
`newTessellateModifier( maxEdgeLength :number, maxIterations :number)`
Constructs a new Tessellate modifier.

## Import

## Properties
- `.maxEdgeLength : number` — The maximum edge length. Default is 0.1 .
- `.maxIterations : number` — The maximum edge length. Default is 0.1 .

## Methods
- `.modify( geometry :BufferGeometry) :BufferGeometry` — Returns a new, modified version of the given geometry by applying a tesselation.
Please note that the resulting geometry is always non-indexed.

## Source