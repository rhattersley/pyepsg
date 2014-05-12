# (C) British Crown Copyright 2011 - 2012, Met Office
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

import xml.etree.ElementTree as ET

import requests


EPSG_IO_URL = 'http://epsg.io/'


class ProjectedCRS(object):
    def __init__(self, element):
        self.element = element

    def as_proj4(self):
        id = self.element.attrib['{http://www.opengis.net/gml/3.2}id']
        code = id.split('-')[-1]
        url = '{prefix}{code}.proj4?download'.format(prefix=EPSG_IO_URL,
                                                     code=code)
        return requests.get(url).text

    def domain(self):
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
    url = '{prefix}{code}.gml?download'.format(prefix=EPSG_IO_URL, code=code)
    xml = requests.get(url).text
    root = ET.fromstring(xml)
    if root.tag == '{http://www.opengis.net/gml/3.2}ProjectedCRS':
        return ProjectedCRS(root)
    raise ValueError('Unsupported code type: {}'.format(root.tag))
