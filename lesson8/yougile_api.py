import requests


class YouGileAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://ru.yougile.com/api-v2"

    def create_project(self, title, users):
        url = f"{self.base_url}/projects"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(url, json=payload, headers=headers)
        return response

    def update_project(self, project_id, title=None, users=None, deleted=None):
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        if deleted is not None:
            payload["deleted"] = deleted

        response = requests.put(url, json=payload, headers=headers)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response

    def delete_project(self, project_id):
        """Удаление проекта через обновление с deleted=True"""
        return self.update_project(project_id, deleted=True)