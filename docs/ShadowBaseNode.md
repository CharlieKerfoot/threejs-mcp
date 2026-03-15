# ShadowBaseNode
Extends: EventDispatcher→Node→

Base class for all shadow nodes. Shadow nodes encapsulate shadow related logic and are always coupled to lighting nodes.
Lighting nodes might share the same shadow node type or use specific ones depending on
their requirements.

## Constructor
`newShadowBaseNode( light :Light)`
Constructs a new shadow base node.

## Properties
- `.isShadowBaseNode : boolean` — This flag can be used for type testing. Default is true .
- `.light :Light` — The shadow casting light.
- `.updateBeforeType : string` — Overwritten since shadows are updated by default per render. Default is 'render' .

## Methods
- `.setupShadowPosition( object :NodeBuilder)` — Setups the shadow position node which is by default the predefined TSL node object shadowPositionWorld .

## Source