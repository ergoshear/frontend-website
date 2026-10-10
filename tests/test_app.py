import unittest

from fastapi.testclient import TestClient

from app.main import app


class WebsiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.close()

    def test_homepage(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        self.assertIn("Ergoshear", response.text)
        self.assertIn('href="https://ergoshear.dev/"', response.text)
        self.assertIn('href="/static/style.css"', response.text)

    def test_stylesheet(self) -> None:
        response = self.client.get("/static/style.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/css", response.headers["content-type"])
        self.assertIn("@media (max-width: 600px)", response.text)

    def test_healthcheck(self) -> None:
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_missing_pages_and_assets(self) -> None:
        for path in ("/missing", "/static/missing.css", "/docs", "/openapi.json"):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 404)


if __name__ == "__main__":
    unittest.main()
