# PDBLoader
Extends: Loader→

A loader for the PDB format. The Protein Data Bank file format is a textual file describing the three-dimensional structures of molecules.

## Constructor
`newPDBLoader( manager :LoadingManager)`
Constructs a new PDB loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded PDB asset
to the onLoad() callback.
- `.parse( text :string) : Object` — Parses the given PDB data and returns an object holding the atoms and
bond geometries as well as the raw atom data as JSON.

## Source