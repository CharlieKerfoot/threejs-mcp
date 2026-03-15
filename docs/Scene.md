# Scene
Extends: EventDispatcher→Object3D→

Scenes allow you to set up what is to be rendered and where by three.js.
This is where you place 3D objects like meshes, lines or lights.

## Constructor
`newScene()`
Constructs a new scene.

## Properties
- `.background :Color|Texture` — Defines the background of the scene. Valid inputs are: A color for defining a uniform colored background. A texture for defining a (flat) textured background. Cube textures or equirectangular textu...
- `.backgroundBlurriness : number` — Sets the blurriness of the background. Only influences environment maps
assigned to Scene#background . Valid input is a float between 0 and 1 . Default is 0 .
- `.backgroundIntensity : number` — Attenuates the color of the background. Only applies to background textures. Default is 1 .
- `.backgroundRotation :Euler` — The rotation of the background in radians. Only influences environment maps
assigned to Scene#background . Default is (0,0,0) .
- `.environment :Texture` — Sets the environment map for all physical materials in the scene. However,
it's not possible to overwrite an existing texture assigned to the envMap material property. Default is null .
- `.environmentIntensity : number` — Attenuates the color of the environment. Only influences environment maps
assigned to Scene#environment . Default is 1 .
- `.environmentRotation :Euler` — The rotation of the environment map in radians. Only influences physical materials
in the scene when Scene#environment is used. Default is (0,0,0) .
- `.fog :Fog|FogExp2` — A fog instance defining the type of fog that affects everything
rendered in the scene. Default is null .
- `.isScene : boolean` — This flag can be used for type testing. Default is true .
- `.overrideMaterial :Material` — Forces everything in the scene to be rendered with the defined material. It is possible
to exclude materials from override by setting Material#allowOverride to false . Default is null .

## Source