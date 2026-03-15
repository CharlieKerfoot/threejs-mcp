# STLLoader
Extends: Loader→

A loader for the STL format, as created by Solidworks and other CAD programs. Supports both binary and ASCII encoded files. The loader returns a non-indexed buffer geometry. Limitations: Binary decoding supports "Magics" color format (http://en.wikipedia.org/wiki/STL_(file_format)#Color_in_binary_STL). There is perhaps some question as to how valid it is to always assume little-endian-ness. ASCII decoding assumes file is UTF-8. For binary STLs geometry might contain colors for vertices. To use it: // use the same code to load STL as above
if ( geometry.hasColors ) {
	material = new THREE.MeshPhongMaterial( { opacity: geometry.alpha, vertexColors: true } );
}
const mesh = new THREE.Mesh( geometry, material ); For ASCII STLs containing multiple solids, each solid is assigned to a different group.
Groups can be used to assign a different color by defining an array of materials with the same length of
geometry.groups and passing it to the Mesh constructor: const materials = [];
const nGeometryGroups = geometry.groups.length;
for ( let i = 0; i < nGeometryGroups; i ++ ) {
	const material = new THREE.MeshPhongMaterial( { color: colorMap[ i ], wireframe: false } );
	materials.push( material );
}
const mesh = new THREE.Mesh(geometry, materials);

## Constructor
`newSTLLoader( manager :LoadingManager)`
Constructs a new STL loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded STL asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :BufferGeometry` — Parses the given STL data and returns the resulting geometry.

## Source