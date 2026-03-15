# Info

This renderer module provides a series of statistical information
about the GPU memory and the rendering process. Useful for debugging
and monitoring.

## Constructor
`newInfo()`
Constructs a new info component.

## Properties
- `.autoReset : boolean` — Whether frame related metrics should automatically
be resetted or not. This property should be set to false by apps which manage their own animation loop. They must
then call renderer.info.reset() ...
- `.calls : number` — The number of render calls since the
app has been started. Default is 0 .
- `.compute : Object` — Compute related metrics.
- `.frame : number` — The current frame ID. This ID is managed
by NodeFrame . Default is 0 .
- `.memory : Object` — Memory related metrics.
- `.render : Object` — Render related metrics.

## Methods
- `.dispose()` — Performs a complete reset of the object.
- `.reset()` — Resets frame related metrics.
- `.update( object :Object3D, count :number, instanceCount :number)` — This method should be executed per draw call and updates the corresponding metrics.

## Source