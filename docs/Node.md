# Node
Extends: EventDispatcher→

Base class for all nodes.

## Constructor
`newNode( nodeType :string)`
Constructs a new node.

## Properties
- `.global : boolean` — Whether this node is global or not. This property is relevant for the internal
node caching system. All nodes which should be declared just once should
set this flag to true (a typical example is A...
- `.isNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the node. Default is '' .
- `.needsUpdate : boolean` — Set this property to true when the node should be regenerated. Default is false .
- `.nodeType : string` — The node type. This represents the result type of the node (e.g. float or vec3 ). Default is null .
- `.parents : boolean` — Create a list of parents for this node during the build process. Default is false .
- `.stackTrace : string` — The stack trace of the node for debugging purposes. Default is null .
- `.type : string` — The type of the class. The value is usually the constructor name.
- `.updateAfterType : string` — The update type of the node's Node#updateAfter method. Possible values are listed in NodeUpdateType . Default is 'none' .
- `.updateBeforeType : string` — The update type of the node's Node#updateBefore method. Possible values are listed in NodeUpdateType . Default is 'none' .
- `.updateType : string` — The update type of the node's Node#update method. Possible values are listed in NodeUpdateType . Default is 'none' .
- `.uuid : string` — The UUID of the node.
- `.version : number` — The version of the node. The version automatically is increased when Node#needsUpdate is set to true . Default is 0 .
- `.captureStackTrace : boolean` — Enables or disables the automatic capturing of stack traces for nodes. Default is false .

## Methods
- `.analyze( builder :NodeBuilder, output :Node)` — Represents the analyze stage which is the second step of the build process, see Node#build method.
This stage analyzes the node hierarchy and ensures descendent nodes are built.
- `.build( builder :NodeBuilder, output :string |Node) :Node| string` — This method performs the build of a node. The behavior and return value depend on the current build stage: setup : Prepares the node and its children for the build process. This process can also cr...
- `.customCacheKey() : number` — Generate a custom cache key for this node.
- `.deserialize( json :Object)` — Deserializes the node from the given JSON.
- `.dispose()` — Calling this method dispatches the dispose event. This event can be used
to register event listeners for clean up tasks.
- `.generate( builder :NodeBuilder, output :string) : string` — Represents the generate stage which is the third step of the build process, see Node#build method.
This state builds the output node and returns the resulting shader string.
- `.getArrayCount( builder :NodeBuilder) : number` — Returns the number of elements in the node array.
- `.getCacheKey( force :boolean, ignores :Set.<Node>) : number` — Returns the cache key for this node.
- `.getChildren() :Node` — Generator function that can be used to iterate over the child nodes.
- `.getElementType( builder :NodeBuilder) : string` — Certain types are composed of multiple elements. For example a vec3 is composed of three float values. This method returns the type of
these elements.
- `.getHash( builder :NodeBuilder) : string` — Returns the hash of the node which is used to identify the node. By default it's
the Node#uuid however derived node classes might have to overwrite this method
depending on their implementation.
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Returns the node member type for the given name.
- `.getNodeType( builder :NodeBuilder) : string` — Returns the node's type.
- `.getScope() :Node` — Returns the references to this node which is by default this .
- `.getSerializeChildren() : Generator.<Object>` — Returns the child nodes as a JSON object.
- `.getShared( builder :NodeBuilder) :Node` — This method is used during the build process of a node and ensures
equal nodes are not built multiple times but just once. For example if attribute( 'uv' ) is used multiple times by the user, the b...
- `.getUpdateAfterType() :NodeUpdateType` — Returns the update type of Node#updateAfter .
- `.getUpdateBeforeType() :NodeUpdateType` — Returns the update type of Node#updateBefore .
- `.getUpdateType() :NodeUpdateType` — Returns the update type of Node#update .
- `.isGlobal( builder :NodeBuilder) : boolean` — By default this method returns the value of the Node#global flag. This method
can be overwritten in derived classes if an analytical way is required to determine the
global cache referring to the c...
- `.onFrameUpdate( callback :function) :Node` — Convenient method for defining Node#update . Similar to Node#onUpdate , but
this method automatically sets the update type to FRAME .
- `.onObjectUpdate( callback :function) :Node` — Convenient method for defining Node#update . Similar to Node#onUpdate , but
this method automatically sets the update type to OBJECT .
- `.onReference( callback :function) :Node` — Convenient method for defining Node#updateReference .
- `.onRenderUpdate( callback :function) :Node` — Convenient method for defining Node#update . Similar to Node#onUpdate , but
this method automatically sets the update type to RENDER .
- `.onUpdate( callback :function, updateType :string) :Node` — Convenient method for defining Node#update .
- `.serialize( json :Object)` — Serializes the node to JSON.
- `.setup( builder :NodeBuilder) :Node` — Represents the setup stage which is the first step of the build process, see Node#build method.
This method is often overwritten in derived modules to prepare the node which is used as a node's out...
- `.toJSON( meta :Object) : Object` — Serializes the node into the three.js JSON Object/Scene format.
- `.traverse( callback :traverseCallback)` — Can be used to traverse through the node's hierarchy.
- `.update( frame :NodeFrame) : boolean` — The method can be implemented to update the node's internal state when it is used to render an object.
The Node#updateType property defines how often the update is executed.
- `.updateAfter( frame :NodeFrame) : boolean` — The method can be implemented to update the node's internal state after it was used to render an object.
The Node#updateAfterType property defines how often the update is executed.
- `.updateBefore( frame :NodeFrame) : boolean` — The method can be implemented to update the node's internal state before it is used to render an object.
The Node#updateBeforeType property defines how often the update is executed.
- `.updateReference( state :any) :any` — Nodes might refer to other objects like materials. This method allows to dynamically update the reference
to such objects based on a given state (e.g. the current node frame or builder).

## Source