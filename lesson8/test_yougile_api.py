import pytest
from yougile_api import YouGileAPI

# Тестовые данные
VALID_API_TOKEN = "hc5Kko8m8X4sq+hHIBJ2dHvLlNv2v99nKjaV7UAkacxaeaLeyyiAdJzkhEmFd0oB"  # Замените на реальный токен
INVALID_API_TOKEN = "1"
TEST_PROJECT_TITLE = "Новый проект"
TEST_USERS = {
    "ab332847-d7ed-4bef-8962-77c36b137a08": "admin"
}


@pytest.fixture
def api_client():
    return YouGileAPI(VALID_API_TOKEN)


@pytest.fixture
def test_project(api_client):
    # Создаем временный проект для тестов
    response = api_client.create_project(TEST_PROJECT_TITLE, TEST_USERS)
    project_id = response.json()["id"]
    yield project_id
    # После теста удаляем проект
    api_client.delete_project(project_id)


class TestYouGileAPI:
    # Тесты для создания проекта
    def test_create_project_success(self, api_client):
        response = api_client.create_project(TEST_PROJECT_TITLE, TEST_USERS)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_unauthorized(self):
        client = YouGileAPI(INVALID_API_TOKEN)
        response = client.create_project(TEST_PROJECT_TITLE, TEST_USERS)
        assert response.status_code == 401

    # Тесты для обновления проекта
    def test_update_project_success(self, api_client, test_project):
        # Обновляем только заголовок
        response = api_client.update_project(test_project, title="Updated Title")
        assert response.status_code == 200

        # Проверяем через GET, что заголовок изменился
        get_response = api_client.get_project(test_project)
        assert get_response.status_code == 200
        assert get_response.json().get("title") == "Updated Title"

    def test_update_project_not_found(self, api_client):
        response = api_client.update_project("nonexistent_id", title="Title")
        assert response.status_code == 404

    # Тесты для получения проекта
    def test_get_project_success(self, api_client, test_project):
        response = api_client.get_project(test_project)
        assert response.status_code == 200
        assert response.json()["id"] == test_project

    def test_get_project_not_found(self, api_client):
        response = api_client.get_project("nonexistent_id")
        assert response.status_code == 404