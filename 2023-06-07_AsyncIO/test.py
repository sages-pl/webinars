from unittest import TestCase, IsolatedAsyncioTestCase
import httpx


BASE_URL = 'https://python3.info'


async def request(method='GET', path='/', data=None, headers=None):
    async with httpx.AsyncClient(base_url=BASE_URL) as ac:
        return await ac.request(method=method, url=path, data=data, headers=headers)


class WebsiteTest(IsolatedAsyncioTestCase):
    async def test_index(self):
        resp = await request('GET', '/index.html')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Matt Harasymczuk', resp.text)
        self.assertIn('Python 3', resp.text)

    async def test_license(self):
        resp = await request('GET', '/LICENSE.html')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Attribution-ShareAlike 4.0 International', resp.text)
        self.assertIn('Creative Commons Attribution-ShareAlike 4.0 International Public License', resp.text)

    async def test_install(self):
        resp = await request('GET', '/install.html')
        self.assertEqual(resp.status_code, 200)
        with self.subTest('Python Versions'):
            self.assertNotIn('3.8', resp.text)
            self.assertNotIn('3.9', resp.text)
            self.assertIn('3.10', resp.text)
            self.assertIn('3.11', resp.text)
        with self.subTest('PyCharm Versions'):
            self.assertNotIn('2022.2', resp.text)
            self.assertNotIn('2022.3', resp.text)
            self.assertIn('2023.1', resp.text)
        with self.subTest('Git Versions'):
            self.assertNotIn('2.31', resp.text)
            self.assertNotIn('2.32', resp.text)
            self.assertIn('2.33', resp.text)
