# NodeFunctionInput

Describes the input of a NodeFunction .

## Constructor
`newNodeFunctionInput( type :string, name :string, count :number, qualifier :'in' | 'out' | 'inout', isConst :boolean)`
Constructs a new node function input.

## Properties
- `.count : number` — If the input is an Array, count will be the length. Default is null .
- `.isConst : boolean` — Whether the input uses a const qualifier or not (only relevant for GLSL). Default is false .
- `.name : string` — The input name.
- `.qualifier : 'in' | 'out' | 'inout'` — The parameter qualifier (only relevant for GLSL). Default is '' .
- `.type : string` — The input type.

## Source