# Copyright (c) 2010-2012, GEM Foundation.
#
# NRML is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NRML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with NRML.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from StringIO import StringIO

from nrml_utils.reader import ExposureTxtReader

class AnExposureTxtReaderShould(unittest.TestCase):

    def setUp(self):
        self.content = StringIO('id,assetCategory,description,stcoType,'
                                'stcoUnit,areaType,areaUnit,cocoType,'
                                'cocoUnit\n'
                                'PAV01,buildings,Collection of existing '
                                'building in downtown Pavia,aggregated,USD,'
                                'per_asset,GBP,per_area,CHF\n\n'
                                'lon,lat,taxonomy,stco,number,area,reco,coco,'
                                'occupants,deductible,limit\n'
                                '28.6925,40.9775,RC_MR_LC,40000,50,1500,4000,'
                                '1000,10,0.05,32000\n'
                                '28.6975,40.9825,RC_MR_LC,300000,100,1000,'
                                '30000,2000,15,0.10,240000')

        self.exp_reader = ExposureTxtReader(self.content)

    def test_read_meta_data(self):
        desc = 'Collection of existing building in downtown Pavia'
        expected_meta_data = dict(
            id='PAV01', assetCategory='buildings', description=desc,
            stcoType='aggregated', stcoUnit='USD', areaType='per_asset',
            areaUnit='GBP', cocoType='per_area', cocoUnit='CHF')

        self.assertEqual(expected_meta_data, self.exp_reader.metadata)

    def test_read_assets(self):
        first_asset = {'area': '1500',
                       'coco': '1000',
                       'deductible': '0.05',
                       'lat': '40.9775',
                       'limit': '32000',
                       'lon': '28.6925',
                       'number': '50',
                       'occupants': '10',
                       'reco': '4000',
                       'stco': '40000',
                       'taxonomy': 'RC_MR_LC'}
        second_asset = {'area': '1000',
                         'coco': '2000',
                         'deductible': '0.10',
                         'lat': '40.9825',
                         'limit': '240000',
                         'lon': '28.6975',
                         'number': '100',
                         'occupants': '15',
                         'reco': '30000',
                         'stco': '300000',
                         'taxonomy': 'RC_MR_LC'}
        expected_assets = [first_asset, second_asset]

        print self.exp_reader.readassets()
        self.assertEqual(expected_assets, self.exp_reader.readassets())