========
SimVideo
========

This EXPERIMENTAL package contains infrastructure to create movies from Cactus 
data. It is based on plugins. To write a new movie, one has to provide a class
that knows how to plot a single frame and load the required data.

The executable is called simvideo. Use the --help option to get a description.
The simvideo/video subfolder contains two examples, one showing how to
plot 2D Cactus data using matplotlib, and one demonstrating the use of VTK.


