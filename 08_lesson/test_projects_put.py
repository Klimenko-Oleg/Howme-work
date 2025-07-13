from projects_api import ProjectsApi


def test_update_project_title(api_client, project_id):
    projects_api = ProjectsApi(api_client)
    response = projects_api.update_project(project_id, "ГосУслуги1")
    print(response.text)
    assert response.status_code == 200


def test_update_project_negative_bad_request(api_client, project_id):
    projects_api = ProjectsApi(api_client)
    body = {"bad_title": "ГосУслуги2"}
    response = api_client.put(
        f'{projects_api.base_url}projects/{project_id}', json=body)
    print(response.text)
    assert response.status_code == 400
