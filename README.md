# telclass

## A Different Way to Study Telecommunications.

### Part I - Symbol Based Simulations

[Class 01: PAM simulation](
 https://github.com/joary/telclass/blob/master/grc/C01_simple_pam)

[Class 02: PSK simulation](
 https://github.com/joary/telclass/blob/master/grc/C02_simple_psk)

[Class 03: QAM simulation](
 https://github.com/joary/telclass/blob/master/grc/C03_simple_qam)

[Class 04: Generic Modulation simulation](
 https://github.com/joary/telclass/blob/master/grc/C04_generic_modulation)

### Part II - Sample Based Simulations

[Class 05: Generic Modulation with Square pulse shaping](
 https://github.com/joary/telclass/blob/master/grc/C05_square_pulse_shaping)

[Class 06: Generic Modulation with Sinc pulse shaping](
    https://github.com/joary/telclass/blob/master/grc/C06_sinc_pulse_shaping)

# Base Infrastructure:

The scripts have been tested with gnuradio version `3.7.11`.

For those who use docker, a precompiled docker container can be found [here]( https://hub.docker.com/r/joarypl/docker-telclass/).

To download the container run:

```
docker pull joarypl/docker-telclass
```

To start the container run:

```
xhost + local:docker
docker run --name telclass \
  -ti --net=host --ulimit rtprio=99 --privileged \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /dev/bus/usb:/dev/bus/usb \
   telclass:latest bash
docker stop telclass
docker rm telclass
```

A new bash terminal will open.
Then navigate to the directory `/home/telclass/grc/` and run any of the existing classes.

```
cd /home/telclass/grc/C01_simple_pam/
gnuradio-companion ./simple_pam.grc
```
