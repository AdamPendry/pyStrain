======
SimRep
======

SimRep is a framework for automated postprocessing of scientific
simulations, in particular tailored to the CACTUS toolkit. The
automatically collected results are combined into an HTML report.
The system is based on postprocessing modules, which call arbitrary
postprocessing scripts, and provide the framework with a template 
to represent the results. For the latter, a python based mini-language
is used, which supports text, figures, tables, lists, and listings of
e.g. logfiles.

Installation
============

Requirements: numpy, scipy, matplotlib, tables

First, install the postcactus python package.
unpack the SimRep tar file and change to the resulting directory.
The install uses the standard python way
python setup.py install --prefix=</where/to/install>
Make sure the resulting package is in the PYTHONPATH environment
variable and the package's bin directory is in the PATH.
For example, if you installed to /usr/local PATH should contain
/usr/local/bin
and PYTHONPATH something like
/usr/local/lib/python2.7/site-packages


Usage
=====
Once installed, you can invoke it with 

simrep --datadir <data path> --repdir <report path> modules

To get usage information, use
simrep --help

For a quick test, run 
simrep --repdir=simrep_examp example

Modules
=======
The modules which are called by simrep are placed in the plugins 
directory of the package. The actual postprocessing scripts are
in the same directory where simrep resides. To install your own 
plugins, just copy the module and script files to those directories.
You can use the existing modules as a template, e.g. the example plugin.

