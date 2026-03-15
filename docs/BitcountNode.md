# BitcountNode
Extends: EventDispatcher→Node→TempNode→MathNode→

This node represents an operation that counts the bits of a piece of shader data.

## Constructor
`newBitcountNode( method :'countTrailingZeros' | 'countLeadingZeros' | 'countOneBits', aNode :Node)`
Constructs a new math node.

## Properties
- `.isBitcountNode : boolean` — This flag can be used for type testing. Default is true .

## Source