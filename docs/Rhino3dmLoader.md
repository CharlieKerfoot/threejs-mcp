# Rhino3dmLoader
Extends: Loader→

A loader for Rhinoceros 3D files and objects. Rhinoceros is a 3D modeler used to create, edit, analyze, document, render,
animate, and translate NURBS curves, surfaces, breps, extrusions, point clouds,
as well as polygon meshes and SubD objects. rhino3dm.js is compiled to WebAssembly
from the open source geometry library openNURBS . The loader currently uses rhino3dm.js 8.4.0 .

## Constructor
`newRhino3dmLoader( manager :LoadingManager)`
Constructs a new Rhino 3DM loader.

## Import

## Methods
- `.debug()` — Prints debug messages to the browser console.
- `.decodeObjects( buffer :ArrayBuffer, url :string) : Promise.<Object3D>` — Decodes the 3DM asset data with a Web Worker.
- `.dispose()` — Frees internal resources. This method should be called
when the loader is no longer required.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded 3DM asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer, onLoad :function, onError :onErrorCallback)` — Parses the given 3DM data and passes the loaded 3DM asset
to the onLoad() callback.
- `.setLibraryPath( path :string) :Rhino3dmLoader` — Path to a folder containing the JS and WASM libraries.
- `.setWorkerLimit( workerLimit :number) :Rhino3dmLoader` — Sets the maximum number of Web Workers to be used during decoding.
A lower limit may be preferable if workers are also for other
tasks in the application.

## Source