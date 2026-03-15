# GCodeLoader
Extends: Loader→

A loader for the GCode format. GCode files are usually used for 3D printing or CNC applications.

## Constructor
`newGCodeLoader( manager :LoadingManager)`
Constructs a new GCode loader.

## Import

## Properties
- `.splitLayer : boolean` — Whether to split layers or not. Default is false .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded GCode asset
to the onLoad() callback.
- `.parse( data :string) :Group` — Parses the given GCode data and returns a group with lines.

## Source