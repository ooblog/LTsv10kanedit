#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
/mnt/home/Tahrpup605/wine-portable-1.7.18-1-p4/wine-portable msiexec /i "/mnt/home/Tahrpup605/wine-portable-1.7.18-1-p4/wine-data/drive_c/installexe/python-3.4.4.msi"
