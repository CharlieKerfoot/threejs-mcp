# Timer

This class is an alternative to Clock with a different API design and behavior.
The goal is to avoid the conceptual flaws that became apparent in Clock over time. Timer has an update() method that updates its internal state. That makes it possible to
call getDelta() and getElapsed() multiple times per simulation step without getting different values. The class can make use of the Page Visibility API to avoid large time delta values when the app
is inactive (e.g. tab switched or browser hidden).

## Constructor
`newTimer()`
Constructs a new timer.

## Methods
- `.connect( document :Document)` — Connect the timer to the given document.Calling this method is not mandatory to
use the timer but enables the usage of the Page Visibility API to avoid large time
delta values.
- `.disconnect()` — Disconnects the timer from the DOM and also disables the usage of the Page Visibility API.
- `.dispose()` — Can be used to free all internal resources. Usually called when
the timer instance isn't required anymore.
- `.getDelta() : number` — Returns the time delta in seconds.
- `.getElapsed() : number` — Returns the elapsed time in seconds.
- `.getTimescale() : number` — Returns the timescale.
- `.reset() :Timer` — Resets the time computation for the current simulation step.
- `.setTimescale( timescale :number) :Timer` — Sets the given timescale which scale the time delta computation
in update() .
- `.update( timestamp :number) :Timer` — Updates the internal state of the timer. This method should be called
once per simulation step and before you perform queries against the timer
(e.g. via getDelta() ).

## Source