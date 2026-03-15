# BlendMode

Represents blending configuration. This class encapsulates all blending-related properties that control how
a material's colors are combined with the colors already in the frame buffer.

## Constructor
`newBlendMode( blending :NoBlending|NormalBlending|AdditiveBlending|SubtractiveBlending|MultiplyBlending|CustomBlending|MaterialBlending)`
Constructs a new blending configuration.

## Properties
- `.blendDst :ZeroFactor|OneFactor|SrcColorFactor|OneMinusSrcColorFactor|SrcAlphaFactor|OneMinusSrcAlphaFactor|DstAlphaFactor|OneMinusDstAlphaFactor|DstColorFactor|OneMinusDstColorFactor|SrcAlphaSaturateFactor|ConstantColorFactor|OneMinusConstantColorFactor|ConstantAlphaFactor|OneMinusConstantAlphaFactor` — Defines the blending destination factor. This determines how the destination (existing) fragment color in the frame buffer
is factored before being combined with the source (incoming) fragment colo...
- `.blendDstAlpha :ZeroFactor|OneFactor|SrcColorFactor|OneMinusSrcColorFactor|SrcAlphaFactor|OneMinusSrcAlphaFactor|DstAlphaFactor|OneMinusDstAlphaFactor|DstColorFactor|OneMinusDstColorFactor|SrcAlphaSaturateFactor|ConstantColorFactor|OneMinusConstantColorFactor|ConstantAlphaFactor|OneMinusConstantAlphaFactor` — Defines the blending destination alpha factor. When set, this allows separate control of the alpha channel's destination blending factor.
If null , BlendMode#blendDst is used for the alpha channel ...
- `.blendEquation :AddEquation|SubtractEquation|ReverseSubtractEquation|MinEquation|MaxEquation` — Defines the blending equation. This determines how the source and destination colors are combined. Default is AddEquation .
- `.blendEquationAlpha :AddEquation|SubtractEquation|ReverseSubtractEquation|MinEquation|MaxEquation` — Defines the blending equation of the alpha channel. When set, this allows separate control of the alpha channel's blending equation.
If null , BlendMode#blendEquation is used for the alpha channel ...
- `.blendSrc :ZeroFactor|OneFactor|SrcColorFactor|OneMinusSrcColorFactor|SrcAlphaFactor|OneMinusSrcAlphaFactor|DstAlphaFactor|OneMinusDstAlphaFactor|DstColorFactor|OneMinusDstColorFactor|SrcAlphaSaturateFactor|ConstantColorFactor|OneMinusConstantColorFactor|ConstantAlphaFactor|OneMinusConstantAlphaFactor` — Defines the blending source factor. This determines how the source (incoming) fragment color is factored before being added
to the destination (existing) fragment color in the frame buffer. Default...
- `.blendSrcAlpha :ZeroFactor|OneFactor|SrcColorFactor|OneMinusSrcColorFactor|SrcAlphaFactor|OneMinusSrcAlphaFactor|DstAlphaFactor|OneMinusDstAlphaFactor|DstColorFactor|OneMinusDstColorFactor|SrcAlphaSaturateFactor|ConstantColorFactor|OneMinusConstantColorFactor|ConstantAlphaFactor|OneMinusConstantAlphaFactor` — Defines the blending source alpha factor. When set, this allows separate control of the alpha channel's source blending factor.
If null , BlendMode#blendSrc is used for the alpha channel as well. D...
- `.blending :NoBlending|NormalBlending|AdditiveBlending|SubtractiveBlending|MultiplyBlending|CustomBlending|MaterialBlending` — Defines the blending type. It must be set to CustomBlending if custom blending properties like BlendMode#blendSrc , BlendMode#blendDst or BlendMode#blendEquation should have any effect. Default is ...
- `.premultiplyAlpha : boolean` — Defines whether to premultiply the alpha (transparency) value. If true , the RGB color of the texture or material is multiplied by its alpha value.
This is useful for transparent textures/materials...

## Methods
- `.clone() :BlendMode` — Returns a clone of this blending configuration.
- `.copy( source :BlendMode) :BlendMode` — Copies the blending properties from the given source to this instance.

## Source