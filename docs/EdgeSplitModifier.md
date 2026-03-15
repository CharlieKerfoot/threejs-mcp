# EdgeSplitModifier

The modifier can be used to split faces at sharp edges. This allows to compute
normals without smoothing the edges which can lead to an improved visual result.

## Constructor
`newEdgeSplitModifier()`

## Import

## Methods
- `.modify( geometry :BufferGeometry, cutOffAngle :number, tryKeepNormals :boolean) :BufferGeometry` — Returns a new, modified version of the given geometry by applying an edge-split operation.
Please note that the resulting geometry is always indexed.

## Source