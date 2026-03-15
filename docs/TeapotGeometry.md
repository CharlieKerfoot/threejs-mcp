# TeapotGeometry
Extends: EventDispatcher→BufferGeometry→

Tessellates the famous Utah teapot database by Martin Newell into triangles. The teapot should normally be rendered as a double sided object, since for some
patches both sides can be seen, e.g., the gap around the lid and inside the spout. Segments 'n' determines the number of triangles output. Total triangles = 32 2 n n - 8 n
(degenerates at the top and bottom cusps are deleted). Code based on SPD software Created for the Udacity course Interactive Rendering

## Constructor
`newTeapotGeometry( size :number, segments :number, bottom :boolean, lid :boolean, body :boolean, fitLid :boolean, blinn :boolean)`
Constructs a new teapot geometry.

## Import

## Source