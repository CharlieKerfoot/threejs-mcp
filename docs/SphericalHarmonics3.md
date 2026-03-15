# SphericalHarmonics3

Represents a third-order spherical harmonics (SH). Light probes use this class
to encode lighting information. Primary reference: https://graphics.stanford.edu/papers/envmap/envmap.pdf Secondary reference: https://www.ppsloan.org/publications/StupidSH36.pdf

## Constructor
`newSphericalHarmonics3()`
Constructs a new spherical harmonics.

## Properties
- `.coefficients : Array.<Vector3>` — An array holding the (9) SH coefficients.
- `.isSphericalHarmonics3 : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.add( sh :SphericalHarmonics3) :SphericalHarmonics3` — Adds the given SH to this instance.
- `.addScaledSH( sh :SphericalHarmonics3, s :number) :SphericalHarmonics3` — A convenience method for performing SphericalHarmonics3#add and SphericalHarmonics3#scale at once.
- `.clone() :SphericalHarmonics3` — Returns a new spherical harmonics with copied values from this instance.
- `.copy( sh :SphericalHarmonics3) :SphericalHarmonics3` — Copies the values of the given spherical harmonics to this instance.
- `.equals( sh :SphericalHarmonics3) : boolean` — Returns true if this spherical harmonics is equal with the given one.
- `.fromArray( array :Array.<number>, offset :number) :SphericalHarmonics3` — Sets the SH coefficients of this instance from the given array.
- `.getAt( normal :Vector3, target :Vector3) :Vector3` — Returns the radiance in the direction of the given normal.
- `.getIrradianceAt( normal :Vector3, target :Vector3) :Vector3` — Returns the irradiance (radiance convolved with cosine lobe) in the
direction of the given normal.
- `.lerp( sh :SphericalHarmonics3, alpha :number) :SphericalHarmonics3` — Linear interpolates between the given SH and this instance by the given
alpha factor.
- `.scale( s :number) :SphericalHarmonics3` — Scales this SH by the given scale factor.
- `.set( coefficients :Array.<Vector3>) :SphericalHarmonics3` — Sets the given SH coefficients to this instance by copying
the values.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Returns an array with the SH coefficients, or copies them into the provided
array. The coefficients are represented as numbers.
- `.zero() :SphericalHarmonics3` — Sets all SH coefficients to 0 .

## Static Methods
- `.getBasisAt( normal :Vector3, shBasis :Array.<number>)` — Computes the SH basis for the given normal vector.

## Source