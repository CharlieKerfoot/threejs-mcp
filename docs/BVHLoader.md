# BVHLoader
Extends: Loader→

A loader for the BVH format. Imports BVH files and outputs a single Skeleton and AnimationClip .
The loader only supports BVH files containing a single root right now.

## Constructor
`newBVHLoader( manager :LoadingManager)`
Constructs a new BVH loader.

## Import

## Properties
- `.animateBonePositions : boolean` — Whether to animate bone positions or not. Default is true .
- `.animateBoneRotations : boolean` — Whether to animate bone rotations or not. Default is true .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded BVH asset
to the onLoad() callback.
- `.parse( text :string) : Object` — Parses the given BVH data and returns the resulting data.

## Source