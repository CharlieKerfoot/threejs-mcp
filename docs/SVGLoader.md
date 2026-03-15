# SVGLoader
Extends: Loader→

A loader for the SVG format. Scalable Vector Graphics is an XML-based vector image format for two-dimensional graphics
with support for interactivity and animation.

## Constructor
`newSVGLoader( manager :LoadingManager)`
Constructs a new SVG loader.

## Import

## Properties
- `.defaultDPI : number` — Default dots per inch. Default is 90 .
- `.defaultUnit : 'mm' | 'cm' | 'in' | 'pt' | 'pc' | 'px'` — Default unit. Default is 'px' .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded SVG asset
to the onLoad() callback.
- `.parse( text :string) : Object` — Parses the given SVG data and returns the resulting data.

## Static Methods
- `.createShapes( shapePath :ShapePath) : Array.<Shape>` — Creates from the given shape path and array of shapes.
- `.getStrokeStyle( width :number, color :string, lineJoin :'round' | 'bevel' | 'miter' | 'miter-limit', lineCap :'round' | 'square' | 'butt', miterLimit :number) : Object` — Returns a stroke style object from the given parameters.
- `.pointsToStroke( points :Array.<Vector2>, style :Object, arcDivisions :number, minDistance :number) :BufferGeometry` — Creates a stroke from an array of points.
- `.pointsToStrokeWithBuffers( points :Array.<Vector2>, style :Object, arcDivisions :number, minDistance :number, vertices :Array.<number>, normals :Array.<number>, uvs :Array.<number>, vertexOffset :number) : number` — Creates a stroke from an array of points.

## Source