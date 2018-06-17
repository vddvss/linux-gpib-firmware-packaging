#!/bin/bash

# This is just a utility script to generate the download links for the
# README.md file.

specname="linux-gpib-firmware.spec"

rpmverrel=$(rpmspec -q --qf "%{VERSION}-%{RELEASE}\n" -D "dist %{nil}" $specname)
rpmname=$(rpmspec -q -D "dist DISTNAME" $specname)
srpmname=$(rpmspec --srpm -q -D 'dist %{nil}' $specname | sed 's/noarch/src.rpm/')

downloadurl="https://github.com/vddvss/linux-gpib-firmware-packaging/releases/download/$rpmverrel"

distro_link() {
    distrpm="${rpmname/DISTNAME/.$1}.rpm"
    echo -n "[$distrpm]($downloadurl/$distrpm)"
}

echo "Install link:"
echo -e "sudo dnf install \"$downloadurl/${rpmname/DISTNAME/\$(rpm -E %dist)}.rpm\"\n"

echo "Download table:"
cat <<EOF
| Distro         | RPM
| -------------- | ------------------------------------------------------------- 
| Fedora 27      | $(distro_link "fc27")
| Fedora 28      | $(distro_link "fc28")
| Fedora Rawhide | $(distro_link "fc29")
| EPEL 7         | $(distro_link "el7")
| SRPM           | [$srpmname]($downloadurl/$srpmname)
EOF
