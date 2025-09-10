import unittest
from exploratory_testing import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_valid_task(self):
        result = self.manager.add_task("Buy groceries")
        self.assertEqual(result, "Task 'Buy groceries' added.")
        self.assertIn("Buy groceries", self.manager.list_tasks())

    def test_add_duplicate_task(self):
        self.manager.add_task("Buy groceries")
        result = self.manager.add_task("Buy groceries")
        self.assertEqual(result, "Task 'Buy groceries' already exists.")
        self.assertEqual(self.manager.list_tasks().count("Buy groceries"), 1)

    def test_add_invalid_task_empty_string(self):
        result = self.manager.add_task("")
        self.assertEqual(result, "Invalid task. Please provide a non-empty string.")
        self.assertEqual(self.manager.list_tasks(), [])

    def test_remove_existing_task(self):
        self.manager.add_task("Read a book")
        result = self.manager.remove_task("Read a book")
        self.assertEqual(result, "Task 'Read a book' removed.")
        self.assertNotIn("Read a book", self.manager.list_tasks())

    def test_remove_nonexistent_task(self):
        result = self.manager.remove_task("Walk the dog")
        self.assertEqual(result, "Task not found.")

    def test_list_tasks(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.assertEqual(self.manager.list_tasks(), ["Task 1", "Task 2"])

    def test_add_task_with_special_characters(self):
        result = self.manager.add_task("Read a book @ 8pm!")
        self.assertEqual(result, "Task 'Read a book @ 8pm!' added.")
        self.assertIn("Read a book @ 8pm!", self.manager.list_tasks())

if __name__ == "__main__":
    unittest.main()