# NodeVar

NodeBuilder is going to create instances of this class during the build process
of nodes. They represent the final shader variables that are going to be generated
by the builder. A dictionary of node variables is maintained in NodeBuilder#vars for
this purpose.

## Constructor
`newNodeVar( name :string, type :string, readOnly :boolean, count :number)`
Constructs a new node variable.

## Properties
- `.count : number` — The size.
- `.isNodeVar : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the variable.
- `.readOnly : boolean` — The read-only flag.
- `.type : string` — The type of the variable.

## Source