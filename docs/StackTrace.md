# StackTrace

Class representing a stack trace for debugging purposes.

## Constructor
`newStackTrace( stackMessage :Error | string | null)`
Creates a StackTrace instance by capturing and filtering the current stack trace.

## Properties
- `.isStackTrace : boolean` — This flag can be used for type testing. Default is true .
- `.stack : Array.<{fn: string, file: string, line: number, column: number}>` — The stack trace.

## Methods
- `.getError( message :string) : string` — Returns the full error message including the stack trace.
- `.getLocation() : string` — Returns a formatted location string of the top stack frame.

## Source