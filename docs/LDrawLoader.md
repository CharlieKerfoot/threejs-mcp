# LDrawLoader
Extends: Loader→

A loader for the LDraw format. [LDraw](https://ldraw.org/} (LEGO Draw) is an open format specification for describing LEGO and other construction set 3D models. An LDraw asset (a text file usually with extension .ldr, .dat or .txt) can describe just a single construction
piece, or an entire model. In the case of a model the LDraw file can reference other LDraw files, which are
loaded from a library path set with setPartsLibraryPath . You usually download the LDraw official parts library,
extract to a folder and point setPartsLibraryPath to it. Library parts will be loaded by trial and error in subfolders 'parts', 'p' and 'models'. These file accesses
are not optimal for web environment, so a script tool has been made to pack an LDraw file with all its dependencies
into a single file, which loads much faster. See section 'Packing LDraw models'. The LDrawLoader example loads
several packed files. The official parts library is not included due to its large size. LDrawLoader supports the following extensions: !COLOUR: Color and surface finish declarations. BFC: Back Face Culling specification. !CATEGORY: Model/part category declarations. !KEYWORDS: Model/part keywords declarations.

## Constructor
`newLDrawLoader( manager :LoadingManager)`
Constructs a new LDraw loader.

## Import

## Methods
- `.addDefaultMaterials() :LDrawLoader` — Initializes the loader with default materials.
- `.addMaterial( material :Material) :LDrawLoader` — Adds a single material to the loader's material library.
- `.addMaterials( materials :Array.<Material>) :LDrawLoader` — Adds a list of materials to the loader's material library.
- `.clearMaterials() :LDrawLoader` — Clears the loader's material library.
- `.getMainEdgeMaterial() :Material` — Returns the material for the edges main LDraw color.
- `.getMainMaterial() :Material` — Returns the Material for the main LDraw color. For an already loaded LDraw asset, returns the Material associated with the main color code.
This method can be useful to modify the main material of ...
- `.getMaterial( colorCode :string) :Material` — Returns a material for the given color code.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded LDraw asset
to the onLoad() callback.
- `.parse( text :string, onLoad :function, onError :onErrorCallback)` — Parses the given LDraw data and returns the resulting group.
- `.preloadMaterials( url :string) : Promise` — This async method preloads materials from a single LDraw file. In the official
parts library there is a special file which is loaded always the first (LDConfig.ldr)
and contains all the standard co...
- `.setConditionalLineMaterial( type :LDrawConditionalLineMaterial.constructor | LDrawConditionalLineNodeMaterial.constructor) :LDrawLoader` — Sets the conditional line material type which depends on the used renderer.
Use LDrawConditionalLineMaterial when using WebGLRenderer and
LDrawConditionalLineNodeMaterial when using WebGPURenderer .
- `.setFileMap( fileMap :Object.<string, string>) :LDrawLoader` — Sets a map which maps referenced library filenames to new filenames.
If a fileMap is not specified (the default), library parts will be accessed by trial and
error in subfolders 'parts', 'p' and 'm...
- `.setMaterials( materials :Array.<Material>) :LDrawLoader` — Sets the loader's material library. This method clears existing
material definitions.
- `.setPartsLibraryPath( path :string) :LDrawLoader` — This method must be called prior to load() unless the model to load does not reference
library parts (usually it will be a model with all its parts packed in a single file).

## Source