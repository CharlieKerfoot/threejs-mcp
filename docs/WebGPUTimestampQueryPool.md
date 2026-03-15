# WebGPUTimestampQueryPool
Extends: TimestampQueryPool→

Manages a pool of WebGPU timestamp queries for performance measurement.
Extends the base TimestampQueryPool to provide WebGPU-specific implementation.

## Constructor
`newWebGPUTimestampQueryPool( device :GPUDevice, type :string, maxQueries :number)`
Creates a new WebGPU timestamp query pool.

## Methods
- `.allocateQueriesForContext( uid :string) : number` — Allocates a pair of queries for a given render context.
- `.dispose() : Promise` — Dispose of the query pool.
- `.resolveQueriesAsync() : Promise.<number>` — Asynchronously resolves all pending queries and returns the total duration.
If there's already a pending resolve operation, returns that promise instead.

## Source