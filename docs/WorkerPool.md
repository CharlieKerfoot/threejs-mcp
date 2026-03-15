# WorkerPool

A simple pool for managing Web Workers.

## Constructor
`newWorkerPool( pool :number)`
Constructs a new Worker pool.

## Import

## Classes

## Properties
- `.pool : number` — The size of the pool. Default is 4 .
- `.queue : Array.<Object>` — A message queue.
- `.workerCreator : function` — A factory function for creating workers.
- `.workerStatus : number` — The current worker status.
- `.workers : Array.<Worker>` — An array of Workers.
- `.workersResolve : Array.<function()>` — An array with resolve functions for messages.

## Methods
- `.dispose()` — Terminates all Workers of this pool. Call this  method whenever this
Worker pool is no longer used in your app.
- `.postMessage( msg :Object, transfer :Array.<ArrayBuffer>) : Promise` — Post a message to an idle Worker. If no Worker is available,
the message is pushed into a message queue for later processing.
- `.setWorkerCreator( workerCreator :function)` — Sets a function that is responsible for creating Workers.
- `.setWorkerLimit( pool :number)` — Sets the Worker limit

## Source