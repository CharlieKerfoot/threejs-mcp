# NodeFunction

Base class for node functions. A derived module must be implemented
for each supported native shader language. Similar to other Node* modules,
this class is only relevant during the building process and not used
in user-level code.

## Constructor
`newNodeFunction( type :string, inputs :Array.<NodeFunctionInput>, name :string, precision :string)`
Constructs a new node function.

## Properties
- `.inputs : Array.<NodeFunctionInput>` — The function's inputs.
- `.name : string` — The name of the uniform. Default is '' .
- `.precision : string` — The precision qualifier. Default is '' .
- `.type : string` — The node type. This type is the return type of the node function.

## Methods
- `.getCode( name :string) : string` — This method returns the native code of the node function.

## Source