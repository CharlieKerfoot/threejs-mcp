# SSAAPassNode
Extends: EventDispatcher→Node→TempNode→PassNode→

A special render pass node that renders the scene with SSAA (Supersampling Anti-Aliasing).
This manual SSAA approach re-renders the scene ones for each sample with camera jitter and accumulates the results. This node produces a high-quality anti-aliased output but is also extremely expensive because of
its brute-force approach of re-rendering the entire scene multiple times. Reference: https://en.wikipedia.org/wiki/Supersampling

## Constructor
`newSSAAPassNode( scene :Scene, camera :Camera)`
Constructs a new SSAA pass node.

## Import

## Properties
- `.clearAlpha : number` — The clear alpha of the pass. Default is 0 .
- `.clearColor :Color` — The clear color of the pass. Default is 0x000000 .
- `.isSSAAPassNode : boolean` — This flag can be used for type testing. Default is true .
- `.sampleLevel : number` — The sample level specified  as n, where the number of samples is 2^n,
so sampleLevel = 4, is 2^4 samples, 16. Default is 4 .
- `.sampleWeight :UniformNode.<float>` — A uniform node representing the sample weight. Default is 1 .
- `.unbiased : boolean` — Whether rounding errors should be mitigated or not. Default is true .

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the pass is no longer required.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's MRT configuration and quad mesh.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the SSAA effect once per frame.

## Source