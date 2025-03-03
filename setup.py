# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='mandiant_ti_client',
    version='0.1.17',
    packages=['mandiant_threatintel'],
    url='',
    license='',
    author='Chris Hultin',
    author_email='chrishultin@google.com',
    description='A Python Client for Mandiant Advantage Threat Intelligence',
    install_requires=[
        'requests~=2.28.1',
        'responses~=0.21.0',
        'python-dateutil',
        'tenacity',
    ],
)
