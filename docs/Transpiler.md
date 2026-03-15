# Transpiler

A class that transpiles shader code from one language into another. Transpiler can only be used to convert GLSL into TSL right now. It is intended
to support developers when they want to migrate their custom materials from the
current to the new node-based material system.

## Constructor
`newTranspiler( decoder :GLSLDecoder, encoder :TSLEncoder)`
Constructs a new transpiler.

## Import

## Properties
- `.decoder : GLSLDecoder` — The GLSL decoder. This component parse GLSL and produces
a language-independent AST for further processing.
- `.encoder : TSLEncoder` — The TSL encoder. It takes the AST and emits TSL code.
- `.linker : Linker` — The linker. It processes the AST and resolves
variable and function references, ensuring that all
dependencies are properly linked.

## Methods
- `.parse( source :string) : string` — Parses the given GLSL source and returns TSL syntax.

## Source