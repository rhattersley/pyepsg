pyepsg
======

|build_status|


A simple interface to http://epsg.io/

For example, we can request the details for EPSG code 21781
"Swiss CH1903 / LV03"::

    >>> projection = pyepsg.get(21781)
    >>> projection.as_proj4()
    +proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=600000 +y_0=200000 +ellps=bessel +towgs84=674.4,15.1,405.3,0,0,0,0 +units=m +no_defs
    >>> projection.domain()
    [5.97, 10.49, 45.83, 47.81]


.. |build_status| image:: https://secure.travis-ci.org/rhattersley/pyepsg.png
   :alt: Build Status
   :target: http://travis-ci.org/rhattersley/pyepsg
