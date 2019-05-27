# Tutorial python and rospy in ROSVITA Graph

In this tutorial we try to explain some inner workings of python and the ROSVITA Graph
itself to motivate some patterns how to use python and rospy in ROSVITA Graphs.

## Python in ROSVITA Graph

First we start with one of the most important aspects of python in ROSVITA Graphs and this is how to use python scripts in them. The answer is pretty simple, add a python script to your ROSVITA project. Then open a ROSVITA Graph instance and drag and drop the script into it. Then just click on Python3.PythonScriptFile and you ready to go.

If the Python Module within the Graph instance is highlighted in red a problem while loading
the python module occurs. This could have several reasons, imports of specific modules are not possible, definition of the method which should be called in the graph is not correct or
just syntactic errors. To get more information just click on th module and read the parserError in the properties window.

If an import was not possible make sure the necessary library is installed or all necessary file are available in the project. We recommend to install all available python libraries with help of [pip](https://docs.python.org/3/installing/index.html). If you have created some python files which should be imported, we recommend to place them under lib/python/ in a ROSVITA project. This is possible due to the properties of the python instance which runs in a ROSVITA Graph. The python instance in a ROSVITA Graph includes the complete project file system to its PYTHONPATH, therefore all files in it can be used and imported in the ROSVITA Graph Python Modules. To do so use the path from Project root to file to import it e.g.

```python
import lib.python.example_lib
```

## Properties python imports and how to use them

Now we know how to use python in ROSVITA Graphs in generell. Next we will explain the inner workings of [imports](https://docs.python.org/3/reference/import.html) in python and how we can use same in a ROSVITA Graph.
