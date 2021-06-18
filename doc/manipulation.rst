Manipulation of Volume Distribution
***********************************

The Volume of Distribution is calculated in the below written fashion:

Manipulating Necessary Data
===========================

#. The :math:`X` is taken from the DoseData.
#. The lnConcData is made by applying :math:`log` to each element of ConcData.
#. The ConcTimeData is made by multiplying ConcData with TimeData.
#. The :math:`k_{el}` is calculated by linear regression

Calculating Volume Distribution
===============================