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
# along with pyepsg.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='pyepsg',
    version='0.5.0',
    url='https://github.com/rhattersley/pyepsg',
    author='Richard Hattersley',
    author_email='rhattersley@gmail.com',
    classifiers=['License :: OSI Approved :: '
                 'GNU Lesser General Public License v3 (LGPLv3)',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Scientific/Engineering :: GIS'],
    description='Easy access to the EPSG database via https://epsg.io/',
    long_description=open('README.rst').read(),
    install_requires=['requests'],
    py_modules=['pyepsg'],
)
