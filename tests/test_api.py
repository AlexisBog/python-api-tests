import pytest
import allure

@allure.feature("Posts API")
class TestPosts:

    @allure.story("Get all posts")
    @allure.title("Отримання списку всіх постів (status 200, count 100)")
    def test_get_all_posts(self, api_client):
        response = api_client.get("/posts")
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) == 100

    @allure.story("Get single post")
    @allure.title("Отримання конкретного посту за ID=10")
    def test_get_single_post(self, api_client):
        response = api_client.get("/posts/10")
        assert response.status_code == 200
        data = response.json()
        
        assert data["id"] == 10
        for field in ["userId", "id", "title", "body"]:
            assert field in data

    @allure.story("Create post")
    @allure.title("Створення нового посту через POST")
    def test_create_post(self, api_client):
        payload = {
            "title": "my title",
            "body": "my body",
            "userId": 1
        }
        response = api_client.post("/posts", json=payload)
        assert response.status_code == 201
        
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]
        assert "id" in data

    @allure.story("Update post")
    @allure.title("Повне оновлення посту через PUT (id=5)")
    def test_update_post_put(self, api_client):
        payload = {
            "id": 5,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        response = api_client.put("/posts/5", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "updated title"

    @allure.story("Partial update post")
    @allure.title("Часткове оновлення title через PATCH (id=5)")
    def test_update_post_patch(self, api_client):
        payload = {
            "title": "patched title"
        }
        response = api_client.patch("/posts/5", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "patched title"

    @allure.story("Delete post")
    @allure.title("Видалення посту через DELETE (id=5)")
    def test_delete_post(self, api_client):
        response = api_client.delete("/posts/5")
        assert response.status_code in [200, 204]

    @allure.story("Negative: Nonexistent post")
    @allure.title("Отримання неіснуючого посту (негативний тест)")
    def test_get_nonexistent_post(self, api_client):
        response = api_client.get("/posts/999999")
        assert response.status_code == 404 or response.json() == {}

    @allure.story("Negative: Empty payload")
    @allure.title("Відправка POST без обов'язкових полів")
    def test_post_empty_payload(self, api_client):
        response = api_client.post("/posts", json={})
        assert response.status_code in [201, 400, 422]

    @allure.story("Headers")
    @allure.title("Перевірка запиту з кастомним заголовком User-Agent")
    def test_request_with_custom_headers(self, api_client):
        headers = {
            "User-Agent": "QA Student"
        }
        response = api_client.get("/posts", headers=headers)
        assert response.status_code == 200


@allure.feature("Todos API")
class TestTodos:

    @allure.story("Get todos by user")
    @allure.title("Фільтрація завдань (todos) за userId=2")
    def test_get_todos_by_user_id(self, api_client):
        response = api_client.get("/todos", params={"userId": 2})
        assert response.status_code == 200
        todos = response.json()
        
        assert len(todos) > 0
        for todo in todos:
            assert todo["userId"] == 2