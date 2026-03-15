# NodeUniform

NodeBuilder is going to create instances of this class during the build process
of nodes. They represent the final shader uniforms that are going to be generated
by the builder. A dictionary of node uniforms is maintained in NodeBuilder#uniforms for this purpose.

## Constructor
`newNodeUniform( name :string, type :string, node :UniformNode)`
Constructs a new node uniform.

## Properties
- `.groupNode :UniformGroupNode` — The uniform node's group.
- `.id : number` — The id of the uniform node.
- `.isNodeUniform : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the uniform.
- `.node :UniformNode` — An reference to the node.
- `.type : string` — The type of the uniform.
- `.value :any` — The value of the uniform node.

## Source