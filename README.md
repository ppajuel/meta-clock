# meta-clock
The layer contains a new bitbake target, core-image-clock, that allows to an embeded device as a smart clock

## Hardware used
The Hardware used for this project is:
* Beaglebone green wireless from Seeedstudio
* 4DCAPE-70T from 4D Systems
* BT Mini-Receiver from Logitech
* LogiLink from C-Media Electronics
* 8 ohms 0,5 W speaker

## Software used
Based on TI AM335x Linux SDK release 4.0. More information [here](http://processors.wiki.ti.com/index.php?title=Processor_SDK_Linux_Release_Notes&oldid=229931). In order to build this software, follow this [wiki page](http://processors.wiki.ti.com/index.php?title=Processor_SDK_Building_The_SDK&oldid=229652) and before to compile the any operating system with bitbake: git clone meta-clock to sources directory, add meta-clock to bblayers.conf file and compile operating system using "MACHINE=beaglebone bitbake core-image-clock" command.

Once the image has beed compiled, the result is located at tisdk/build/arago-tmp-external-linaro-toolchain/deploy/images/beaglebone/core-image-clock-beaglebone.tar.xz.Use igep-media-create from [igep-tools](https://github.com/ppajuel/igep-tools
) to burn a sd card image:
* Machine parameter can be igep0034 machine.
* Image parameter should be core-image-clock-beaglebone.tar.xz.
* Mmc parameter should be the sd /dev device.

### QT application
qt-clock binary has been compiled using  meta-toolchain-arago-tisdk for beaglebone MACHINE from TI AM335x Linux SDK release 4.0. qt-clock source is located [here](https://github.com/gil9red/DigitalClock_cpp_qml).

## Tun operating system
Take care that emmc first sector should be erased or BOOT button must be pressed during boot up in order to boot from SD card.
BT Mini-Receiver acts by default as a bluetooth HID receiver, in order to configure as a HCI device is necessary to press user botton during bootup.
