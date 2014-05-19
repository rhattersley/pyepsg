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

    >>> print projection.as_proj4()
    +proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=600000 +y_0=200000 +ellps=bessel +towgs84=674.4,15.1,405.3,0,0,0,0 +units=m +no_defs
    >>> print projection.as_wkt()
    PROJCS["CH1903 / LV03",GEOGCS["CH1903",DATUM["CH1903",SPHEROID["Bessel 1841",6377397.155,299.1528128,AUTHORITY["EPSG","7004"]],TOWGS84[674.4,15.1,405.3,0,0,0,0],AUTHORITY["EPSG","6149"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4149"]],PROJECTION["Hotine_Oblique_Mercator_Azimuth_Center"],PARAMETER["latitude_of_center",46.95240555555556],PARAMETER["longitude_of_center",7.439583333333333],PARAMETER["azimuth",90],PARAMETER["rectified_grid_angle",90],PARAMETER["scale_factor",1],PARAMETER["false_easting",600000],PARAMETER["false_northing",200000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Y",EAST],AXIS["X",NORTH],AUTHORITY["EPSG","21781"]]

.. |build_status| image:: https://secure.travis-ci.org/rhattersley/pyepsg.png
   :alt: Build Status
   :target: http://travis-ci.org/rhattersley/pyepsg
