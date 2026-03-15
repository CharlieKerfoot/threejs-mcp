# Volume

This class had been written to handle the output of the NRRDLoader .
It contains a volume of data and information about it. For now it only handles 3 dimensional data.

## Constructor
`newVolume( xLength :number, yLength :number, zLength :number, type :string, arrayBuffer :ArrayBuffer)`
Constructs a new volume.

## Import

## Properties
- `.RASDimensions : Array.<number>` — This array holds the dimensions of the volume in the RAS space
- `.axisOrder : Array.<string>` — The order of the Axis dictated by the NRRD header
- `.data : TypedArray` — The data of the volume.
- `.inverseMatrix : Martrix3` — The RAS to IJK matrix.
- `.lowerThreshold : number` — The voxels with values under this threshold won't appear in the slices.
If changed, geometryNeedsUpdate is automatically set to true on all the slices associated to this volume.
- `.matrix : Martrix3` — The IJK to RAS matrix.
- `.offset : Array.<number>` — Offset of the volume in the RAS coordinate system
- `.segmentation : boolean` — Whether to use segmentation mode or not.
It can load 16-bits nrrds correctly. Default is false .
- `.sliceList : Array.<VolumeSlice>` — The list of all the slices associated to this volume
- `.spacing : Array.<number>` — Spacing to apply to the volume from IJK to RAS coordinate system
- `.upperThreshold : number` — The voxels with values over this threshold won't appear in the slices.
If changed, geometryNeedsUpdate is automatically set to true on all the slices associated to this volume
- `.xLength : number` — Width of the volume in the IJK coordinate system. Default is 1 .
- `.yLength : number` — Height of the volume in the IJK coordinate system. Default is 1 .
- `.zLength : number` — Depth of the volume in the IJK coordinate system. Default is 1 .

## Methods
- `.access( i :number, j :number, k :number) : number` — Compute the index in the data array corresponding to the given coordinates in IJK system.
- `.computeMinMax() : Array.<number>` — Compute the minimum and the maximum of the data in the volume.
- `.extractPerpendicularPlane( axis :'x' | 'y' | 'z', RASIndex :number) : Object` — Compute the orientation of the slice and returns all the information relative to the geometry such as sliceAccess,
the plane matrix (orientation and position in RAS coordinate) and the dimensions o...
- `.extractSlice( axis :'x' | 'y' | 'z', index :number) :VolumeSlice` — Returns a slice corresponding to the given axis and index.
The coordinate are given in the Right Anterior Superior coordinate format.
- `.getData( i :number, j :number, k :number) : number` — Shortcut for data[access(i,j,k)].
- `.map( functionToMap :function, context :Object) :Volume` — Apply a function to all the voxels, be careful, the value will be replaced.
- `.repaintAllSlices() :Volume` — Call repaint on all the slices extracted from this volume.
- `.reverseAccess( index :number) : Array.<number>` — Retrieve the IJK coordinates of the voxel corresponding of the given index in the data.

## Source