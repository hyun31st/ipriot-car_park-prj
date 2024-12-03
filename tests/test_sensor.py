import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestEntryAndExitSensor(unittest.TestCase):
    '''
    Test Entry and Exit Sensor classes
    '''
    def setUp(self):
        '''
        Initiate classes for testing
        '''
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        '''
        Check EntrySensor initialized with all attributes
        '''
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_exit_sensor_initialized_with_all_attributes(self):
        '''
        Check ExitSensor initialized with all attributes
        '''
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_entry_and_exit_sensor_update_car_park(self):
        '''
        Check update_car_park method of EntrySensor and ExitSensor
        '''
        self.entry_sensor.update_car_park("Test-001")
        self.assertIn("Test-001", self.car_park.plates)  # check the plate entered
        self.exit_sensor.update_car_park("Test-001")
        self.assertNotIn("Test-001", self.car_park.plates) # check the plate exit


if __name__ == '__main__':
    unittest.main()