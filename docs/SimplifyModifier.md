# SimplifyModifier

This class can be used to modify a geometry by simplifying it. A typical use
case for such a modifier is automatic LOD generation. The implementation is based on Progressive Mesh type Polygon Reduction Algorithm by Stan Melax in 1998.

## Constructor
`newSimplifyModifier()`

## Import

## Methods
- `.modify( geometry :BufferGeometry, count :number) :BufferGeometry` — Returns a new, modified version of the given geometry by applying a simplification.
Please note that the resulting geometry is always non-indexed.

## Source