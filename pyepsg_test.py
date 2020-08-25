import unittest
import pyepsg
import datetime

class TestAll(unittest.TestCase):

    def test_get_cached(self):
        #on first pass, cache wont be live, so it will take longer (will fetch from URL)
        start_time = datetime.datetime.now()
        proj1 = pyepsg.get(21781)
        e = datetime.datetime.now() - start_time
        self.assertGreater(e.total_seconds(), 0.01)
        self.assertTrue('PROJCS["CH1903_LV03",GEOGCS["GCS_CH1903",DATUM["D_CH1903",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Hotine_Oblique_Mercator_Azimuth_Center"],PARAMETER["latitude_of_center",46.95240555555556],PARAMETER["longitude_of_center",7.439583333333333],PARAMETER["azimuth",90],PARAMETER["scale_factor",1],PARAMETER["false_easting",600000],PARAMETER["false_northing",200000],UNIT["Meter",1]]', proj1.as_esri_wkt())

        #now it must be immediate as cache was already populated
        start_time = datetime.datetime.now()
        proj2 = pyepsg.get(21781)
        e = datetime.datetime.now() - start_time
        self.assertLess(e.total_seconds(), 0.01)
        self.assertTrue('PROJCS["CH1903_LV03",GEOGCS["GCS_CH1903",DATUM["D_CH1903",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Hotine_Oblique_Mercator_Azimuth_Center"],PARAMETER["latitude_of_center",46.95240555555556],PARAMETER["longitude_of_center",7.439583333333333],PARAMETER["azimuth",90],PARAMETER["scale_factor",1],PARAMETER["false_easting",600000],PARAMETER["false_northing",200000],UNIT["Meter",1]]', proj2.as_esri_wkt())

        #the projection from first and cache results must be the same
        self.assertEqual(proj1, proj2)

        h1 = proj1.as_html
        h2 = proj1.as_html
        self.assertEqual(h1, h2)

        h1 = proj1.as_html
        h2 = proj1.as_html
        self.assertEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()
