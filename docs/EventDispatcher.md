# EventDispatcher

This modules allows to dispatch event objects on custom JavaScript objects. Main repository: eventdispatcher.js Code Example:

## Constructor
`newEventDispatcher()`

## Methods
- `.addEventListener( type :string, listener :function)` — Adds the given event listener to the given event type.
- `.dispatchEvent( event :Object)` — Dispatches an event object.
- `.hasEventListener( type :string, listener :function) : boolean` — Returns true if the given event listener has been added to the given event type.
- `.removeEventListener( type :string, listener :function)` — Removes the given event listener from the given event type.

## Source