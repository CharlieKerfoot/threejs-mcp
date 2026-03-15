# CodeNode
Extends: EventDispatcher→Node→

This class represents native code sections. It is the base
class for modules like FunctionNode which allows to implement
functions with native shader languages.

## Constructor
`newCodeNode( code :string, includes :Array.<Node>, language :'js' | 'wgsl' | 'glsl')`
Constructs a new code node.

## Properties
- `.code : string` — The native code. Default is '' .
- `.global : boolean` — This flag is used for global cache. Default is true .
- `.includes : Array.<Node>` — An array of includes Default is [] .
- `.isCodeNode : boolean` — This flag can be used for type testing. Default is true .
- `.language : 'js' | 'wgsl' | 'glsl'` — The used language. Default is '' .

## Methods
- `.getIncludes( builder :NodeBuilder) : Array.<Node>` — Returns the includes of this code node.
- `.setIncludes( includes :Array.<Node>) :CodeNode` — Sets the includes of this code node.

## Source