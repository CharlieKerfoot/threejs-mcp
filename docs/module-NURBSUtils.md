# NURBSUtils

## Import

## Methods
- `.calcBSplineDerivatives( p :number, U :Array.<number>, P :Array.<Vector4>, u :number, nd :number) : Array.<Vector4>` — Calculates derivatives of a B-Spline. See The NURBS Book, page 93, algorithm A3.2.
- `.calcBSplinePoint( p :number, U :Array.<number>, P :Array.<Vector4>, u :number) :Vector4` — Calculates B-Spline curve points. See The NURBS Book, page 82, algorithm A3.1.
- `.calcBasisFunctionDerivatives( span :number, u :number, p :number, n :number, U :Array.<number>) : Array.<Array.<number>>` — Calculates basis functions derivatives. See The NURBS Book, page 72, algorithm A2.3.
- `.calcBasisFunctions( span :number, u :number, p :number, U :Array.<number>) : Array.<number>` — Calculates basis functions. See The NURBS Book, page 70, algorithm A2.2.
- `.calcKoverI( k :number, i :number) : number` — Calculates "K over I".
- `.calcNURBSDerivatives( p :number, U :Array.<number>, P :Array.<Vector4>, u :number, nd :number) : Array.<Vector3>` — Calculates NURBS curve derivatives. See The NURBS Book, page 127, algorithm A4.2.
- `.calcRationalCurveDerivatives( Pders :Array.<Vector4>) : Array.<Vector3>` — Calculates derivatives (0-nd) of rational curve. See The NURBS Book, page 127, algorithm A4.2.
- `.calcSurfacePoint( p :number, q :number, U :Array.<number>, V :Array.<number>, P :Array.<Array.<Vector4>>, u :number, v :number, target :Vector3) (inner)` — Calculates a rational B-Spline surface point. See The NURBS Book, page 134, algorithm A4.3.
- `.calcVolumePoint( p :number, q :number, r :number, U :Array.<number>, V :Array.<number>, W :Array.<number>, P :Array.<Array.<Array.<Vector4>>>, u :number, v :number, w :number, target :Vector3) (inner)` — Calculates a rational B-Spline volume point. See The NURBS Book, page 134, algorithm A4.3.
- `.findSpan( p :number, u :number, U :Array.<number>) : number` — Finds knot vector span.

## Source