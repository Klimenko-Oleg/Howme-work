from projects_api import ProjectsApi


def test_create(api_client):
    projects_api = ProjectsApi(api_client)
    response = projects_api.create_project("ГосУслуги2")
    print(response.text)
    assert response.status_code == 201


def test_create_negative_missing_field(api_client):
    projects_api = ProjectsApi(api_client)
    response = api_client.post(
        f'{projects_api.base_url}projects', json={})
    print(response.text)
    assert response.status_code == 400
