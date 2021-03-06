# Djuke - PreAmplifier v2.0

This is the C source code for a modular preamplifier, so the features depend a lot on the different pcb's that are used. The heart of the preamp is the PreampController pcb, which connects the other pcb's, display, buttons, encoder, infrared receiver, etc. Other sensible configurations are:

- Standalone stereo or 5.1 input selection (switch inputs using buttons and infrared, no volume control)
- Standalone DAC in software mode (volume is controlled by the DAC)
- Standalone VolumeControl (without input selection, so single input)
- Combinations of the above (e.g. 5.1 input selection + volume control)
 - Stereo input selection + volume control
 - Stereo + 5.1 input selection + volume control
 - Stereo input selection + DAC + volume control
 - Stereo +5.1 input selection + DAC + volume control
 - DAC + volume control

## Links

[PreAmplifier project page](http://www.djuke.nl/en/projects/10-pre-amplifiers/34-preamplifierv2)

[PreAmplifier products](http://www.djuke.nl/index.php?page=shop.browse&category_id=67&vmcchk=1&option=com_virtuemart&Itemid=8)

[PreAmplifier support pages](http://www.djuke.nl/en/support/15-preamplifier)

## Building

Building the software is done in Linux and requires SDCC (small device C Compiler) to be installed. From the source code directory, simply run:

```
make
```

If no errors occurred, this will result in DjukePreampV2.hex being generated. Temporary files can be removed using:

```
make clean
```

## Changelog

### version 0.9
Release date: 2016-02-15
- Interrupt based infrared
- Visualisation if input level
- Detection of elapsed time without signal
- Support different hardware setups
- Loading/saving from/to eeprom
- Set RC5 infrared address
- Auto switch off function when silent for a long time
- Uptime, ontime and standby time information
- Generic parameter settings
- Terminal support for controlling preamp from UART
- InputSelect and DAC can be used standalong (without VolumeControl)
- Event based control (buttons, encoder, infrared, etc)
- Added DAC error codes
- Support for (chained) 8channel VolumeControl pcbs (up to 24 channels)
- Display title from UART
- Increased number of DAC inputs to 5 (to be used by Raspberry Pi)

### version 1.0
Release date: 2016-04-18
- Added makefile for compiling from command line
- Added new style configuration bits
- Handle UART at high priority
- Set title only for specific input
- Added python tools for integration with Volumio/Rune
- Improved debug mechanism
- Switch on power to have backlight in hardware setup menu

### version 1.1
Release date: 2016-12-21
- Python script now python3 compatible
- Added 'spare' to list of inputs
- Defined input names as array to save space

