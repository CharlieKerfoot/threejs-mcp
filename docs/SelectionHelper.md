# SelectionHelper

A helper for SelectionBox . It visualizes the current selection box with a div container element.

## Constructor
`newSelectionHelper( renderer :WebGPURenderer|WebGLRenderer, cssClassName :string)`
Constructs a new selection helper.

## Import

## Properties
- `.element : HTMLDivElement` — The visualization of the selection box.
- `.enabled : boolean` — Whether helper is enabled or not. Default is true .
- `.isDown : boolean` — Whether the mouse or pointer is pressed down. Default is false .
- `.renderer :WebGPURenderer|WebGLRenderer` — A reference to the renderer.

## Methods
- `.dispose()` — Call this method if you no longer want use to the controls. It frees all internal
resources and removes all event listeners.

## Source