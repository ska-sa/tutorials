Radio Astronomy tutorials
==========================

Various IPython notebook based lecture notes and tutorials developed at SKA SA.

Static versions of the notebooks can be accessed using [nbviewer](http://nbviewer.ipython.org), for the full SKA SA tutorial repository [here](http://nbviewer.ipython.org/github/ska-sa/tutorials/tree/master).

(0) **Introduction to the notebook** 
<br/>
Short introduction to using the ipython notebook.

(1) **Introduction to Radio Astronomy** (~3 hour tutorial) 
<br/>
Introduction to Radio Astronomy using data from the KAT-7 radio telescope.

(2) **Radio Astronomy honours/graduate course** (semester long) 
<br/>
This lecture material and these tutorials were used in the [NASSP](http://www.star.ac.za) honours course in Radio Astronomy. The course broadly follows the NRAO [Essential Radio Astronomy](http://www.cv.nrao.edu/course/astr534/ERA.shtml) course.

(3) **Interferometry workshop**
<br/>
Notebook material from a week long Radio Interferometry workshop, first developed for the 2015 NWU Radio Interferometry Winter School.

(4) **HartRAO Spectral Line**
<br>
Python tutorials on reducing methanol maser monitoring data from HartRAO. A two week course given at the Ghana Space Science and Technology Institute (GSSTI) as part of the Royal Society radio astronomy capacity building program in Ghana.

(5) **Machine Learning**
<br>
Introduction to some basic machine learning notebooks.


##Building your own docker container with the tutorials##
**This requires you to have a docker engine system running on your localhost**

Once you have cloned this repository locally with:

```
git clone https://github.com/ska-sa/tutorials.git
```

build the image with:

```
docker build -t tuts .
```

Note: If you are having build issues that report 'unable to resolve archive.ubuntu.com' or similar errors, try the following build command instead:

```
docker build -t tuts --network=host .
```

run the container with:
```
docker run -d -p 8888:8888 tuts start-notebook.sh --NotebookApp.token=''
```

you should now be able to access the notebooks from http://localhost:8888

**This will run the notebook without any authentication. For more detail on this see [Jupyter Docker Stacks](https://github.com/Paperspace/jupyter-docker-stacks/tree/master/scipy-notebook)**

