#!/bin/bash
echo -e "install python dependencies"
sudo python3 -m pip install -r requirements.txt

echo -e "source local catkin ws"
cd catkin_ws 
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.5m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.5m.so
cd ..
source catkin_ws/devel/setup.bash --extend

echo -e "Fin"
