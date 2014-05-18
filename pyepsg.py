# (C) British Crown Copyright 2014, Met Office
#
# This file is part of pyepsg.
#
# pyepsg is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyepsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyepsg.  If not, see <http://www.gnu.org/licenses/>.
"""
Provides simple access to http://epsg.io/.

The entry point for this package is the :func:`get()` function.

"""

import xml.etree.ElementTree as ET

import requests


EPSG_IO_URL = 'http://epsg.io/'


class ProjectedCRS(object):
    """
    Represents a single projected CRS.

    """
    def __init__(self, element):
        self.element = element

    @property
    def id(self):
        id = self.element.attrib['{http://www.opengis.net/gml/3.2}id']
        code = id.split('-')[-1]
        return code

    def as_esri_wkt(self):
        """
        Return the ESRI WKT string which corresponds to the projection.

        For example::

            >>> print get(27700).as_esri_wkt() + '...'
        PROJCS["OSGB_1936_British_National_Grid",GEOGCS["GCS_OSGB 19...

        """
        url = '{prefix}{code}.esriwkt?download'.format(prefix=EPSG_IO_URL,
                                                       code=self.id)
        return requests.get(url).text

    def as_html(self):
        """
        Return the OGC WKT which corresponds to the projection as HTML.

        For example::

            >>> print get(27700).as_html() + '...'
        <div class="syntax"><pre><span class="gh">PROJCS</span><span...

        """
        url = '{prefix}{code}.html?download'.format(prefix=EPSG_IO_URL,
                                                    code=self.id)
        return requests.get(url).text

    def as_proj4(self):
        """
        Return the PROJ.4 string which corresponds to the projection.

        For example::

            >>> get(21781).as_proj4()
            +proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 \
+k_0=1 +x_0=600000 +y_0=200000 +ellps=bessel \
+towgs84=674.4,15.1,405.3,0,0,0,0 +units=m +no_defs

        """
        url = '{prefix}{code}.proj4?download'.format(prefix=EPSG_IO_URL,
                                                     code=self.id)
        return requests.get(url).text

    def as_wkt(self):
        """
        Return the OGC WKT string which corresponds to the projection.

        For example::

            >>> print get(27700).as_wkt() + '...'
        PROJCS["OSGB 1936 / British National Grid",GEOGCS["OSGB 1936...

        """
        url = '{prefix}{code}.wkt?download'.format(prefix=EPSG_IO_URL,
                                                   code=self.id)
        return requests.get(url).text

    def domain(self):
        """
        Return the domain of validity for this projection as:
        (west, east, south, north).

        For example::

            >>> get(21781).domain()
            [5.97, 10.49, 45.83, 47.81]


        """
        # TODO: Check for gmd:EX_GeographicBoundingBox and blow up otherwise.
        # TODO: Generalise interface to return a polygon? (Can we find
        # something that uses a polygon instead?)
        domain = self.element.find(
            '{http://www.opengis.net/gml/3.2}domainOfValidity')
        domain_href = domain.attrib['{http://www.w3.org/1999/xlink}href']
        url = '{prefix}{code}.gml?download'.format(prefix=EPSG_IO_URL,
                                                   code=domain_href)
        xml = requests.get(url).text
        gml = ET.fromstring(xml.encode('UTF-8'))

        def extract_bound(i, tag):
            # TODO: Figure out if this is our problem or ET's.
            # `find` isn't returning anything :(
            #ns = '{http://www.isotc211.org/2005/gmd}'
            #bound = gml.find(ns + tag)
            bound = gml[1][0][1][0][i]
            return float(bound[0].text)

        tags = ('westBoundLongitude', 'eastBoundLongitude',
                'southBoundLatitude', 'northBoundLatitude')
        bounds = [extract_bound(i, tag) for i, tag in enumerate(tags)]
        return bounds


def get(code):
    """
    Return an object that corresponds to the given EPSG code.

    Currently supported object types are:
        - :class:`ProjectedCRS`

    For example::

        projection = get(27700)

    """
    url = '{prefix}{code}.gml?download'.format(prefix=EPSG_IO_URL, code=code)
    xml = requests.get(url).text
    root = ET.fromstring(xml)
    if root.tag == '{http://www.opengis.net/gml/3.2}ProjectedCRS':
        return ProjectedCRS(root)
    raise ValueError('Unsupported code type: {}'.format(root.tag))
