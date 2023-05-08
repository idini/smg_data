from lib.storage.FakeStorageManager import FakeStorageManager

class TestFakeStorageManager():

    @classmethod
    def setup_class (cls):
        """ """
        pass

    @classmethod
    def teardown_class (cls):
        """ """
        pass

    ### Method setup/teardown

    def setup_method (self):
        """ """
        self.fake_storage_manager = FakeStorageManager()

    def teardown_method(self):
        """ """

        del self.fake_storage_manager

    ### Tests

    def test_read_data (self):

        test_id = 16793

        expected_item = "Adriana Lima"

        result = self.fake_storage_manager.read(test_id)

        assert (result == expected_item)

    def test_write_data (self):

        test_item = "SentenCe ExamPle"
        test_id = 0

        self.fake_storage_manager.write(test_id, test_item)

        result = self.fake_storage_manager.read(test_id)

        assert (result == test_item)