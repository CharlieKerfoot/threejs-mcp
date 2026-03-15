# ProgressiveLightMap

Progressive Light Map Accumulator, by zalo . To use, simply construct a ProgressiveLightMap object, plmap.addObjectsToLightMap(object) an array of semi-static
objects and lights to the class once, and then call plmap.update(camera) every frame to begin accumulating
lighting samples. This should begin accumulating lightmaps which apply to
your objects, so you can start jittering lighting to achieve
the texture-space effect you're looking for. This class can only be used with WebGLRenderer .
When using WebGPURenderer , import from ProgressiveLightMapGPU.js .

## Constructor
`newProgressiveLightMap( renderer :WebGLRenderer, res :number)`
Constructs a new progressive light map.

## Import

## Properties
- `.renderer :WebGLRenderer` — The renderer.
- `.res : number` — The side-long dimension of the total lightmap. Default is 1024 .

## Methods
- `.addObjectsToLightMap( objects :Array.<Object3D>)` — Sets these objects' materials' lightmaps and modifies their uv1's.
- `.dispose()` — Frees all internal resources.
- `.showDebugLightmap( visible :boolean, position :Vector3)` — Draws the lightmap in the main scene. Call this after adding the objects to it.
- `.update( camera :Camera, blendWindow :number, blurEdges :boolean)` — This function renders each mesh one at a time into their respective surface maps.

## Source