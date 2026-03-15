# EXRExporter

An exporter for EXR. EXR ( Extended Dynamic Range) is an open format specification for professional-grade image storage format of the motion picture industry. The purpose of
format is to accurately and efficiently represent high-dynamic-range scene-linear image data
and associated metadata. The library is widely used in host application software where accuracy
is critical, such as photorealistic rendering, texture access, image compositing, deep compositing,
and DI.

## Constructor
`newEXRExporter()`

## Import

## Methods
- `.parse( arg1 :DataTexture|WebGPURenderer|WebGLRenderer, arg2 :EXRExporter~Options|RenderTarget, arg3 :EXRExporter~Options) : Promise.<Uint8Array>` — This method has two variants. When exporting a data texture, it receives two parameters. The texture and the exporter options. When exporting a render target (e.g. a PMREM), it receives three param...

## Type Definitions
- `.Options` — Export options of EXRExporter .

## Source