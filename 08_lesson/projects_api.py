class ProjectsApi:
    def __init__(self, api_client, base_url=None):
        self.api_client = api_client
        self.base_url = base_url or "https://yougile.com/api-v2/"

    def create_project(self, title):
        """Создает новый проект."""
        body = {"title": title}
        response = self.api_client.post(
            f"{self.base_url}projects", json=body)
        return response

    def get_project(self, project_id):
        """Получает проект по ID."""
        response = self.api_client.get(
            f"{self.base_url}projects/{project_id}")
        return response

    def update_project(self, project_id, title):
        """Обновляет название проекта."""
        body = {"title": title}
        response = self.api_client.put(
            f"{self.base_url}projects/{project_id}", json=body)
        return response
