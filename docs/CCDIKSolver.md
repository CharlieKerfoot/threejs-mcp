# CCDIKSolver

This class solves the Inverse Kinematics Problem with a CCD Algorithm . CCDIKSolver is designed to work with instances of SkinnedMesh .

## Constructor
`newCCDIKSolver( mesh :SkinnedMesh, iks :Array.<CCDIKSolver~IK>)`

## Import

## Properties
- `.iks : Array.<CCDIKSolver~IK>` — The IK objects.
- `.mesh :SkinnedMesh` — The skinned mesh.

## Methods
- `.createHelper( sphereSize :number) :CCDIKHelper` — Creates a helper for visualizing the CCDIK.
- `.update( globalBlendFactor :number) :CCDIKSolver` — Updates all IK bones by solving the CCD algorithm.
- `.updateOne( ik :CCDIKSolver~IK, overrideBlend :number) :CCDIKSolver` — Updates one IK bone solving the CCD algorithm.

## Type Definitions
- `.BoneLink` — This type represents bone links.
- `.IK` — This type represents IK configuration objects.

## Source