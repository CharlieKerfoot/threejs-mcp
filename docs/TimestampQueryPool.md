# TimestampQueryPool

Abstract base class of a timestamp query pool.

## Constructor
`newTimestampQueryPool( maxQueries :number)(abstract)`
Creates a new timestamp query pool.

## Properties
- `.currentQueryIndex : number` — How many queries allocated so far. Default is 0 .
- `.frames : Array.<number>` — Stores all timestamp frames.
- `.isDisposed : boolean` — Whether the pool has been disposed or not. Default is false .
- `.lastValue : number` — The total frame duration until the next update. Default is 0 .
- `.maxQueries : number` — Maximum number of queries this pool can hold. Default is 256 .
- `.pendingResolve : boolean | Promise.<number>` — This property is used to avoid multiple concurrent resolve operations.
The WebGL backend uses it as a boolean flag. In context of WebGPU, it holds
the promise of the current resolve operation. Defa...
- `.queryOffsets : Map.<string, number>` — Tracks offsets for different contexts.
- `.timestamps : Map.<string, number>` — Stores the latest timestamp for each render context.
- `.trackTimestamp : boolean` — Whether to track timestamps or not. Default is true .

## Methods
- `.allocateQueriesForContext( uid :string, frameId :number) : number` — Allocate queries for a specific uid.
- `.dispose() (abstract)` — Dispose of the query pool.
- `.getTimestamp( uid :string) : number` — Returns the timestamp for a given render context.
- `.getTimestampFrames() : Array.<number>` — Returns all timestamp frames.
- `.hasTimestamp( uid :string) : boolean` — Returns whether a timestamp is available for a given render context.
- `.resolveQueriesAsync() : Promise.<number> | number` — Resolve all timestamps and return data (or process them).

## Source