import unittest
import httpx

class TestMicroservicesAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for the API endpoints
        self.base_url = "http://localhost:8000"

    def test_create_question(self):
        data = {
            "title": "Sample Question",
            "text": "This is a sample question.",
            "author": "John Doe"
        }
        response = httpx.post(f"{self.base_url}/questions/", json=data)
        self.assertEqual(response.status_code, 200)
        question = response.json()["question"]
        self.assertEqual(question["title"], "Sample Question")
        self.assertEqual(question["text"], "This is a sample question.")
        self.assertEqual(question["author"], "John Doe")

    def test_get_questions(self):
        response = httpx.get(f"{self.base_url}/questions/")
        self.assertEqual(response.status_code, 200)
        questions = response.json()
        self.assertIsInstance(questions, list)

    def test_get_question(self):
        # Assuming there is a question with ID 1 in the database
        response = httpx.get(f"{self.base_url}/questions/1")
        self.assertEqual(response.status_code, 200)
        question = response.json()
        self.assertEqual(question["id"], 1)

    def test_update_question(self):
        data = {
            "title": "Updated Question",
            "text": "This question has been updated.",
            "author": "Jane Smith"
        }
        response = httpx.put(f"{self.base_url}/questions/1", json=data)
        self.assertEqual(response.status_code, 200)
        updated_question = response.json()["question"]
        self.assertEqual(updated_question["title"], "Updated Question")
        self.assertEqual(updated_question["text"], "This question has been updated.")
        self.assertEqual(updated_question["author"], "Jane Smith")

    def test_delete_question(self):
        # Assuming there is a question with ID 1 in the database
        response = httpx.delete(f"{self.base_url}/questions/1")
        self.assertEqual(response.status_code, 200)
        message = response.json()["message"]
        self.assertEqual(message, "Question deleted successfully")

if __name__ == "__main__":
    unittest.main()
