# Euler

A class representing Euler angles. Euler angles describe a rotational transformation by rotating an object on
its various axes in specified amounts per axis, and a specified axis
order. Iterating through an instance will yield its components (x, y, z,
order) in the corresponding order.

## Constructor
`newEuler( x :number, y :number, z :number, order :string)`
Constructs a new euler instance.

## Properties
- `.isEuler : boolean` — This flag can be used for type testing. Default is true .
- `.order : string` — A string representing the order that the rotations are applied. Default is 'XYZ' .
- `.x : number` — The angle of the x axis in radians. Default is 0 .
- `.y : number` — The angle of the y axis in radians. Default is 0 .
- `.z : number` — The angle of the z axis in radians. Default is 0 .
- `.DEFAULT_ORDER : string` — The default Euler angle order. Default is 'XYZ' .

## Methods
- `.clone() :Euler` — Returns a new Euler instance with copied values from this instance.
- `.copy( euler :Euler) :Euler` — Copies the values of the given Euler instance to this instance.
- `.equals( euler :Euler) : boolean` — Returns true if this Euler instance is equal with the given one.
- `.fromArray( array :Array.<number, number, number, ?string>) :Euler` — Sets this Euler instance's components to values from the given array. The first three
entries of the array are assign to the x,y and z components. An optional fourth entry
defines the Euler order.
- `.reorder( newOrder :string) :Euler` — Resets the euler angle with a new order by creating a quaternion from this
euler angle and then setting this euler angle with the quaternion and the
new order. Warning: This discards revolution inf...
- `.set( x :number, y :number, z :number, order :string) :Euler` — Sets the Euler components.
- `.setFromQuaternion( q :Quaternion, order :string, update :boolean) :Euler` — Sets the angles of this Euler instance from a normalized quaternion.
- `.setFromRotationMatrix( m :Matrix4, order :string, update :boolean) :Euler` — Sets the angles of this Euler instance from a pure rotation matrix.
- `.setFromVector3( v :Vector3, order :string) :Euler` — Sets the angles of this Euler instance from the given vector.
- `.toArray( array :Array.<number, number, number, string>, offset :number) : Array.<number, number, number, string>` — Writes the components of this Euler instance to the given array. If no array is provided,
the method returns a new instance.

## Source