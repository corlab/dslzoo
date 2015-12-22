query.py
========

query.py is a Python script that performs a number of queries to Google Scholar for the [Survey on Domain-Specific Languages in Robotics](http://link.springer.com/chapter/10.1007%2F978-3-319-11900-7_17) and the [Robotics DSL Zoo](http://corlab.github.io/dslzoo/).


Dependendies
------------

The script builds upon [scholar.py](https://github.com/norro/scholar.py) by Christian Kreibich, in a patched version available [here](https://github.com/norro/scholar.py).


Note
----

The script will perform a large number of queries (>>100) to Google Scholar and will result in getting blocked when not pausing for an appropriate time between each query. Please consider adapting the script accordingly before using.

