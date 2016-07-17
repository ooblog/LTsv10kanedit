#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
cd ..
/mnt/home/Tahrpup605/wine-portable-1.7.18-1-p4/wine-portable "/mnt/home/Tahrpup605/wine-portable-1.7.18-1-p4/wine-data/drive_c/Python34/python.exe kanedit.py"
