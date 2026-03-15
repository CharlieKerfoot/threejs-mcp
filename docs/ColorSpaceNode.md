# ColorSpaceNode
Extends: EventDispatcher→Node→TempNode→

This node represents a color space conversion. Meaning it converts
a color value from a source to a target color space.

## Constructor
`newColorSpaceNode( colorNode :Node, source :string, target :string)`
Constructs a new color space node.

## Properties
- `.colorNode :Node` — Represents the color to convert.
- `.source : string` — The source color space.
- `.target : string` — The target color space.

## Methods
- `.resolveColorSpace( builder :NodeBuilder, colorSpace :string) : string` — This method resolves the constants WORKING_COLOR_SPACE and OUTPUT_COLOR_SPACE based on the current configuration of the
color management and renderer.

## Source