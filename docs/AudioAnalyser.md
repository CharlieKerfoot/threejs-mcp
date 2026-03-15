# AudioAnalyser

This class can be used to analyse audio data.

## Constructor
`newAudioAnalyser( audio :Audio, fftSize :number)`
Constructs a new audio analyzer.

## Properties
- `.analyser : AnalyserNode` — The global audio listener.
- `.data : Uint8Array` — Holds the analyzed data.

## Methods
- `.getAverageFrequency() : number` — Returns the average of the frequencies returned by AudioAnalyser#getFrequencyData .
- `.getFrequencyData() : Uint8Array` — Returns an array with frequency data of the audio. Each item in the array represents the decibel value for a specific frequency.
The frequencies are spread linearly from 0 to 1/2 of the sample rate...

## Source