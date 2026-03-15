# WebGLTimestampQueryPool
Extends: TimestampQueryPool→

Manages a pool of WebGL timestamp queries for performance measurement.
Handles creation, execution, and resolution of timer queries using WebGL extensions.

## Constructor
`newWebGLTimestampQueryPool( gl :WebGLRenderingContext | WebGL2RenderingContext, type :string, maxQueries :number)`
Creates a new WebGL timestamp query pool.

## Methods
- `.allocateQueriesForContext( uid :string) : number` — Allocates a pair of queries for a given render context.
- `.beginQuery( uid :string)` — Begins a timestamp query for the specified render context.
- `.dispose()` — Releases all resources held by this query pool.
This includes deleting all query objects and clearing internal state.
- `.endQuery( uid :string)` — Ends the active timestamp query for the specified render context.
- `.resolveQueriesAsync() : Promise.<number>` — Asynchronously resolves all completed queries and returns the total duration.
- `.resolveQuery( query :WebGLQuery) : Promise.<number>` — Resolves a single query, checking for completion and disjoint operation.

## Source