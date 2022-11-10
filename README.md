# nRF5 SDK Docker Container

This repo contains scripts to build docker containers bundling the [nRF5 SDK for Thread and Zigbee](https://www.nordicsemi.com/Products/Development-software/nRF5-SDK-for-Thread-and-Zigbee) with the `arm-none-eabi-gcc` compiler

## Usage Example
Let's compile the example `light_switch` that comes with the nRF5 SDK. In order to compile the example, navigate in the example directory first.

Make sure that `SDK_ROOT` is set to `/sdk` in your Makefile (for instance `pca10056/blank/armgcc`).

You simply need to run the docker container with the make command:

```
docker run \
  -v $(pwd):/work \
  --rm \
  ghcr.io/peterkappelt/nrf5-sdk-zigbee-docker:sdk-4.2.0-gcc-8-2018-q4-major \
  make -Cpca10056/blank/armgcc
```


## Supported versions

Currently, containers are provided for ARM GCC versions: 
  - 8-2018-q4-major
  - 9-2019-q4-major
  - 10-2020-q4-major
  - 10.3-2021.10


and SDK versions:
  - 4.2.0
  - 4.1.0
  - 4.0.0
  - 3.2.0

## Licensing

Though this build utility is licensed with MIT, `arm-none-eabi-gcc` and the nRF5 SDK for Thread and Zigbee are distributed with different licenses.

## Disclaimer
I'm not affiliated with Nordic Semiconductor, this repo just contains tools I'm using for my own projects.