# PCDLoader
Extends: Loader→

A loader for the Point Cloud Data (PCD) format. PCDLoader supports ASCII and (compressed) binary files as well as the following PCD fields: x y z rgb normal_x normal_y normal_z intensity label

## Constructor
`newPCDLoader( manager :LoadingManager)`
Constructs a new PCD loader.

## Import

## Properties
- `.littleEndian : boolean` — Whether to use little Endian or not. Default is true .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded PCD asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :Points` — Parses the given PCD data and returns a point cloud.

## Source