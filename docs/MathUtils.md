# MathUtils

A collection of math utility functions.

## Static Methods
- `.ceilPowerOfTwo( value :number) : number` — Returns the smallest power of two that is greater than or equal to the given number.
- `.clamp( value :number, min :number, max :number) : number` — Clamps the given value between min and max.
- `.damp( x :number, y :number, lambda :number, dt :number) : number` — Smoothly interpolate a number from x to y in  a spring-like manner using a delta
time to maintain frame rate independent movement. For details, see Frame rate independent damping using lerp .
- `.degToRad( degrees :number) : number` — Converts degrees to radians.
- `.denormalize( value :number, array :TypedArray) : number` — Denormalizes the given value according to the given typed array.
- `.euclideanModulo( n :number, m :number) : number` — Computes the Euclidean modulo of the given parameters that
is ( ( n % m ) + m ) % m .
- `.floorPowerOfTwo( value :number) : number` — Returns the largest power of two that is less than or equal to the given number.
- `.generateUUID() : string` — Generate a UUID (universally unique identifier).
- `.inverseLerp( x :number, y :number, value :number) : number` — Returns the percentage in the closed interval [0, 1] of the given value
between the start and end point.
- `.isPowerOfTwo( value :number) : boolean` — Returns true if the given number is a power of two.
- `.lerp( x :number, y :number, t :number) : number` — Returns a value linearly interpolated from two known points based on the given interval - t = 0 will return x and t = 1 will return y .
- `.mapLinear( x :number, a1 :number, a2 :number, b1 :number, b2 :number) : number` — Performs a linear mapping from range <a1, a2> to range <b1, b2> for the given value.
- `.normalize( value :number, array :TypedArray) : number` — Normalizes the given value according to the given typed array.
- `.pingpong( x :number, length :number) : number` — Returns a value that alternates between 0 and the given length parameter.
- `.radToDeg( radians :number) : number` — Converts radians to degrees.
- `.randFloat( low :number, high :number) : number` — Returns a random float from <low, high> interval.
- `.randFloatSpread( range :number) : number` — Returns a random integer from <-range/2, range/2> interval.
- `.randInt( low :number, high :number) : number` — Returns a random integer from <low, high> interval.
- `.seededRandom( s :number) : number` — Returns a deterministic pseudo-random float in the interval [0, 1] .
- `.setQuaternionFromProperEuler( q :Quaternion, a :number, b :number, c :number, order :'XYX' | 'XZX' | 'YXY' | 'YZY' | 'ZXZ' | 'ZYZ')` — Sets the given quaternion from the Intrinsic Proper Euler Angles defined by the given angles and order. Rotations are applied to the axes in the order specified by order:
rotation by angle a is app...
- `.smootherstep( x :number, min :number, max :number) : number` — A variation on smoothstep that has zero 1st and 2nd order derivatives at x=0 and x=1.
- `.smoothstep( x :number, min :number, max :number) : number` — Returns a value in the range [0,1] that represents the percentage that x has
moved between min and max , but smoothed or slowed down the closer x is to
the min and max . See Smoothstep for more det...

## Source