# PropertyMixer

Buffered scene graph property that allows weighted accumulation; used internally.

## Constructor
`newPropertyMixer( binding :PropertyBinding, typeName :string, valueSize :number)`
Constructs a new property mixer.

## Properties
- `.binding :PropertyBinding` — The property binding.
- `.cumulativeWeight : number` — Accumulated weight of the property binding. Default is 0 .
- `.cumulativeWeightAdditive : number` — Accumulated additive weight of the property binding. Default is 0 .
- `.referenceCount : number` — Number of keyframe tracks referencing this property binding. Default is 0 .
- `.useCount : number` — Number of active keyframe tracks currently using this property binding. Default is 0 .
- `.valueSize : number` — The keyframe track value size.

## Methods
- `.accumulate( accuIndex :number, weight :number)` — Accumulates data in the incoming region into accu<i> .
- `.accumulateAdditive( weight :number)` — Accumulates data in the incoming region into add .
- `.apply( accuIndex :number)` — Applies the state of accu<i> to the binding when accus differ.
- `.restoreOriginalState()` — Applies the state previously taken via PropertyMixer#saveOriginalState to the binding.
- `.saveOriginalState()` — Remembers the state of the bound property and copy it to both accus.

## Source