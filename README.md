This repo contains firmware rpms for use with
[linux-gpib rpm packages](https://github.com/vddvss/linux-gpib-packaging).
The firmware packaged in these rpms is from the
[linux-gpib project](https://linux-gpib.sourceforge.io/).

This firmware is required for use with adapters compatible with the:
- NI GPIB-USB-B (the NI GPIB-USB-HS/HS+ do not need firmware)
- HP/Agilent/Keysight:
  - 82341C
  - 82341D
  - 82350A
  - 82357A
  - 82357B

# Installation

```bash
# Install the linux-gpib driver rpms
sudo dnf copr enable vddvss/linux-gpib

# Install the driver:
# For a general installation that will require you to edit the gpib.conf file
sudo dnf install dkms-linux-gpib linux-gpib

# To include a gpib.conf file set up for Agilent/Keysight 82357A/B
sudo dnf install dkms-linux-gpib linux-gpib linux-gpib-defaults-agilent-82357a

# To include a gpib.conf file set up for NI-GPIB-USB-B
sudo dnf install dkms-linux-gpib linux-gpib linux-gpib-defaults-ni-gpib-usb

# Install the firmware (url can be combined with the install commands above)
sudo dnf install "https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1$(rpm -E %dist).noarch.rpm"
```

Or download and install the appropriate rpm:

| Distro         | RPM
| -------------- | ------------------------------------------------------------- 
| Fedora 27      | [linux-gpib-firmware-20080810-1.fc27.noarch.rpm](https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1.fc27.noarch.rpm)
| Fedora 28      | [linux-gpib-firmware-20080810-1.fc28.noarch.rpm](https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1.fc28.noarch.rpm)
| Fedora Rawhide | [linux-gpib-firmware-20080810-1.fc29.noarch.rpm](https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1.fc29.noarch.rpm)
| EPEL 7         | [linux-gpib-firmware-20080810-1.el7.noarch.rpm](https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1.el7.noarch.rpm)
| SRPM           | [linux-gpib-firmware-20080810-1.src.rpm](https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/20080810-1/linux-gpib-firmware-20080810-1.src.rpm)

