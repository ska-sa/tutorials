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

run the container with:
```
docker run -d -p 8888:8888 tuts
```

you should now be able to access the notebooks from http://localhost:8888

##Running the Notebooks on SageMathCloud##
**May be depricated due to the price structure at SageMathCloud**

If you want to run the notebooks without having ipython on your computer, we suggest you try [SageMathCloud](https://cloud.sagemath.com/):

* Create an account on [SageMathCloud](https://cloud.sagemath.com/)
* Start a new project
* Inside your new project, click on "New"
* In the "Name your file or paste in a web link" field, paste the link to this github repo:  https://github.com/ska-sa/tutorials.git 
* Hit enter and wait a minute or so for the tutorials to download
* Click on "Files"
* You should now have the tutorials directory in your project!
* Navigate through the directory and open the notebook you want to work on by clicking on it
* Now run the notebook as normal!
* Notebooks are opened in their own tabs, so you can always go back to "File" and open a new notebook in another tab


