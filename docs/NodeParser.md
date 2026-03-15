# NodeParser

Base class for node parsers. A derived parser must be implemented
for each supported native shader language.

## Constructor
`newNodeParser()`

## Methods
- `.parseFunction( source :string) :NodeFunction` — The method parses the given native code an returns a node function.

## Source