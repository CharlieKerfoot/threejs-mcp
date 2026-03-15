# NodeCache

This utility class is used in NodeBuilder as an internal
cache data structure for node data.

## Constructor
`newNodeCache( parent :NodeCache)`
Constructs a new node cache.

## Properties
- `.id : number` — The id of the cache.
- `.nodesData : WeakMap.<Node, Object>` — A weak map for managing node data.
- `.parent :NodeCache` — Reference to a parent node cache. Default is null .

## Methods
- `.getData( node :Node) : Object` — Returns the data for the given node.
- `.setData( node :Node, data :Object)` — Sets the data for a given node.

## Source