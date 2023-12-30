---
layout: post
title: Install Nvidia Driver On Ubuntu22.04 (Lenovo)
excerpt: Handle SGX, Secure Boot
tags: nvidia lenovo ubuntu sgx mok
---

## Enable SGX

In BIOS, set SGX to Enabled.

## Install Nvidia Driver

Remove Nvidia Packages

``` {.bash}
sudo apt-get remove --purge nvidia-*
sudo apt-get remove --purge '^libnvidia-.*'
sudo apt-get remove --purge '^cuda-.*'
```

Find Drivers

``` {.bash}
ubuntu-drivers devices
```

DO NOT CHOOSE \`nvidia-driver-\*-open\`

Install

``` {.bash}
sudo apt-get install nvidia-driver-525
```

If there is a dialog about \"secure boot\", remember your password

``` {.bash}
sudo reboot
```

## First Reboot

Select \"Perform MOK Management\", Select \"Enroll MOK\", Input your
password, Select \"Ok\"

## Check Driver

``` {.bash}
nvidia-smi
```

## References

-   <https://gist.github.com/bitsurgeon/b0f4440984c9e60dcd8fe8bbc346c029>
-   <https://www.linuxcapable.com/install-nvidia-drivers-on-ubuntu-linux/>

```{=html}
<div id="comments"></div>  
```
