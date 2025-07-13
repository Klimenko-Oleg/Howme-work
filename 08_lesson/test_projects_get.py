from projects_api import ProjectsApi


def test_get_project_by_id_success(api_client, project_id):
    projects_api = ProjectsApi(api_client)
    response = projects_api.get_project(project_id)
    print(response.text)
    assert response.status_code == 200

    project_data = response.json()
    assert "title" in project_data
    assert "id" in project_data
    assert project_data["id"] == project_id


def test_get_project_by_id_not_found(api_client):
    projects_api = ProjectsApi(api_client)
    non_existent_id = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    response = projects_api.get_project(non_existent_id)
    print(response.text)
    assert response.status_code == 404
