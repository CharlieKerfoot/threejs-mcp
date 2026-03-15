# AsciiEffect

A class that creates an ASCII effect. The ASCII generation is based on jsascii .

## Constructor
`newAsciiEffect( renderer :WebGLRenderer, charSet :string, options :AsciiEffect~Options)`
Constructs a new ASCII effect.

## Import

## Properties
- `.domElement : HTMLDivElement` — The DOM element of the effect. This element must be used instead of the
default WebGLRenderer#domElement .

## Methods
- `.render( scene :Object3D, camera :Camera)` — When using this effect, this method should be called instead of the
default WebGLRenderer#render .
- `.setSize( w :number, h :number)` — Resizes the effect.

## Type Definitions
- `.Options` — This type represents configuration settings of AsciiEffect .

## Source