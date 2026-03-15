# MeshSurfaceSampler

Utility class for sampling weighted random points on the surface of a mesh. Building the sampler is a one-time O(n) operation. Once built, any number of
random samples may be selected in O(logn) time. Memory usage is O(n). References: http://www.joesfer.com/?p=84 https://stackoverflow.com/a/4322940/1314762

## Constructor
`newMeshSurfaceSampler( mesh :Mesh)`
Constructs a mesh surface sampler.

## Import

## Methods
- `.build() :MeshSurfaceSampler` — Processes the input geometry and prepares to return samples. Any configuration of the
geometry or sampler must occur before this method is called. Time complexity is O(n)
for a surface with n faces.
- `.sample( targetPosition :Vector3, targetNormal :Vector3, targetColor :Color, targetUV :Vector2) :MeshSurfaceSampler` — Selects a random point on the surface of the input geometry, returning the
position and optionally the normal vector, color and UV Coordinate at that point.
Time complexity is O(log n) for a surfac...
- `.setRandomGenerator( randomFunction :function) :MeshSurfaceSampler` — Allows to set a custom random number generator. Default is Math.random() .
- `.setWeightAttribute( name :string) :MeshSurfaceSampler` — Specifies a vertex attribute to be used as a weight when sampling from the surface.
Faces with higher weights are more likely to be sampled, and those with weights of
zero will not be sampled at al...

## Source