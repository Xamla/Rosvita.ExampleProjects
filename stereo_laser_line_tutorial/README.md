# How to use Stereo Laser Line Client

In this tutorial we explain how to use the StereoLaserLineClient and even more important
point to the prerequisites to be able to use it.

## What the Stereo Laser Line Client does

The StereoLaserLineClient captures images of two cameras which are arange in a stereo setup.
The cameras first capture a image with disabled line laser and after that with enabled laser.
From both images a diff image is computed and after that the 3d points of the laser line is
triangulated. As a result we get the 3d points of the laser line.

# Prerequisites

To use the StereoLaserLineClient we first need a stereo camera setup and in the later application
both cameras need free field of view. Furthermore we need a calibration of the stereo setup to be
able to triangulate the laser line points. And we need a line laser which is connect to one of the
cameras.

Creating a valid and precise stereo calibration is not trivial. To do so we provide a seperate
software package which tries to make the calibration process simpler (LINK necessary!!!!!)

The last prerequisite is that you need at least !!!This!!! Version of ROSVITA to run the
StereoLaserLineClient in the form we showcase here.

So to run the provided example please first create a Stereocalibration of your stereo setup and add
the resulting t7 file to calibration. After that open the file stereo_laser_line_example.py and update all camera serial numbers, the path to the calibration file and io port of the laser.

After that open the ROSVITA Configuration Window and also update the camera serials of the two GeniCam instances.

# Run example

If all prerequisites are met you can just run the example in the console or as an ROSVITA Graph.
Please take into account that in the current implementation the debug mode is switched on. Therefore, the StereoLaserLineClient provide plots of the diff images and the output points and block until you close these windows. In a later productive environment the debug mode has to be switch of.

To run the example from console navigate to the project root then use following command:

```python
python3 stereo_laser_line_example.py
```

To run the Graph just open stereo_laser_line_example.xgraph and run the Graph
