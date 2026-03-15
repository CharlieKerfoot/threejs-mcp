# Controls
Extends: EventDispatcher→

Abstract base class for controls.

## Constructor
`newControls( object :Object3D, domElement :HTMLElement)(abstract)`
Constructs a new controls instance.

## Properties
- `.domElement : HTMLElement` — The HTML element used for event listeners. Default is null .
- `.enabled : boolean` — Whether the controls responds to user input or not. Default is true .
- `.keys : Object` — This object defines the keyboard input of the controls.
- `.mouseButtons : Object` — This object defines what type of actions are assigned to the available mouse buttons.
It depends on the control implementation what kind of mouse buttons and actions are supported.
- `.object :Object3D` — The object that is managed by the controls.
- `.state : number` — The internal state of the controls. Default is -1 .
- `.touches : Object` — This object defines what type of actions are assigned to what kind of touch interaction.
It depends on the control implementation what kind of touch interaction and actions are supported.

## Methods
- `.connect( element :HTMLElement)` — Connects the controls to the DOM. This method has so called "side effects" since
it adds the module's event listeners to the DOM.
- `.disconnect()` — Disconnects the controls from the DOM.
- `.dispose()` — Call this method if you no longer want use to the controls. It frees all internal
resources and removes all event listeners.
- `.update( delta :number)` — Controls should implement this method if they have to update their internal state
per simulation step.

## Source