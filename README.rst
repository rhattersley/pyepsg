pyepsg
======

|build_status|


A simple interface to http://epsg.io/

For example, we can request the details for the projected coordinate system
identified by EPSG code 21781, aka. "Swiss CH1903 / LV03"::

    >>> projection = pyepsg.get(21781)
    >>> projection
    <ProjectedCRS: 21781, CH1903 / LV03>
    >>> projection.domain_of_validity()
    [5.97, 10.49, 45.83, 47.81]
    >>> projection.cartesian_cs.axes
    [<Axis: east / metre>, <Axis: north / metre>]

Projected and geodetic coordinate systems can also be converted to various
other forms::

    >>> print(projection.as_proj4()[:70] + '...')
    +proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 ...
    >>> print(projection.as_wkt()[:70] + '...')
    PROJCS["CH1903 / LV03",GEOGCS["CH1903",DATUM["CH1903",SPHEROID["Bessel...

.. |build_status| image:: https://secure.travis-ci.org/rhattersley/pyepsg.png
   :alt: Build Status
   :target: http://travis-ci.org/rhattersley/pyepsg
