# TextGeometry
Extends: EventDispatcher→BufferGeometry→ExtrudeGeometry→

A class for generating text as a single geometry. It is constructed by providing a string of text, and a set of
parameters consisting of a loaded font and extrude settings. See the FontLoader page for additional details. TextGeometry uses typeface.json generated fonts.
Some existing fonts can be found located in /examples/fonts .

## Constructor
`newTextGeometry( text :string, parameters :TextGeometry~Options)`
Constructs a new text geometry.

## Import

## Type Definitions
- `.Options` — Represents the options type of the geometry's constructor.

## Source