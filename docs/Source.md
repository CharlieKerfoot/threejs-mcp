# Source

Represents the data source of a texture. The main purpose of this class is to decouple the data definition from the texture
definition so the same data can be used with multiple texture instances.

## Constructor
`newSource( data :any)`
Constructs a new video texture.

## Properties
- `.data :any` — The data definition of a texture.
- `.dataReady : boolean` — This property is only relevant when Source#needsUpdate is set to true and
provides more control on how texture data should be processed. When dataReady is set
to false , the engine performs the mem...
- `.id : number` — The ID of the source.
- `.isSource : boolean` — This flag can be used for type testing. Default is true .
- `.needsUpdate : boolean` — When the property is set to true , the engine allocates the memory
for the texture (if necessary) and triggers the actual texture upload
to the GPU next time the source is used. Default is false .
- `.uuid : string` — The UUID of the source.
- `.version : number` — This starts at 0 and counts how many times Source#needsUpdate is set to true . Default is 0 .

## Methods
- `.getSize( target :Vector2|Vector3) :Vector2|Vector3` — Returns the dimensions of the source into the given target vector.
- `.toJSON( meta :Object | string) : Object` — Serializes the source into JSON.

## Source