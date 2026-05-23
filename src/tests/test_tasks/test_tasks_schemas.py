import pytest
from datetime import datetime
from pydantic import ValidationError
from tasks.schemas import (
    TaskBaseSchemas,
    TaskCreateSchemas,
    TaskUpateSchemas,
    TaskResponseSchemas,
)


class TestTaskBaseSchemas:
    def test_valid_task_base(self):
        data = {
            "title": "My Task Title",
            "description": "This is a valid description",
            "is_complated": False,
        }
        task = TaskBaseSchemas(**data)
        assert task.title == "My Task Title"
        assert task.description == "This is a valid description"
        assert task.is_complated is False

    def test_title_min_length_validation(self):
        with pytest.raises(ValidationError) as exc_info:
            TaskBaseSchemas(title="abc", description="desc", is_complated=True)
        errors = exc_info.value.errors()
        # بررسی می‌کنیم که خطایی برای فیلد title وجود داشته باشد و نوع آن 'string_too_short' باشد
        title_errors = [e for e in errors if e['loc'][0] == 'title']
        assert len(title_errors) == 1
        assert title_errors[0]['type'] == 'string_too_short'
        # یا می‌توانید فقط بررسی کنید که هر خطایی رخ داده
        # assert any(e['loc'][0] == 'title' for e in errors)

    def test_title_max_length_validation(self):
        long_title = "a" * 151
        with pytest.raises(ValidationError) as exc_info:
            TaskBaseSchemas(title=long_title, description="desc", is_complated=False)
        errors = exc_info.value.errors()
        title_errors = [e for e in errors if e['loc'][0] == 'title']
        assert len(title_errors) == 1
        assert title_errors[0]['type'] == 'string_too_long'

    def test_description_max_length_validation(self):
        long_desc = "b" * 501
        with pytest.raises(ValidationError) as exc_info:
            TaskBaseSchemas(title="Valid Title", description=long_desc, is_complated=True)
        errors = exc_info.value.errors()
        desc_errors = [e for e in errors if e['loc'][0] == 'description']
        assert len(desc_errors) == 1
        assert desc_errors[0]['type'] == 'string_too_long'

    def test_description_optional_none_allowed(self):
        task = TaskBaseSchemas(title="Valid Title", description=None, is_complated=False)
        assert task.description is None

    def test_description_optional_required_if_provided(self):
        with pytest.raises(ValidationError):
            TaskBaseSchemas(title="Valid", description=123, is_complated=False)

    def test_is_complated_required(self):
        with pytest.raises(ValidationError):
            TaskBaseSchemas(title="Valid Title", description="desc")

    def test_title_required(self):
        with pytest.raises(ValidationError):
            TaskBaseSchemas(description="desc", is_complated=True)


class TestTaskCreateSchemas:
    def test_create_inherits_validation(self):
        data = {"title": "Create Task", "description": "create desc", "is_complated": False}
        task = TaskCreateSchemas(**data)
        assert task.title == "Create Task"
        with pytest.raises(ValidationError):
            TaskCreateSchemas(title="bad", description="desc", is_complated=True)


class TestTaskUpdateSchemas:
    def test_update_inherits_validation(self):
        data = {"title": "Updated Task", "description": "new desc", "is_complated": True}
        task = TaskUpateSchemas(**data)
        assert task.is_complated is True

    def test_update_still_validates(self):
        with pytest.raises(ValidationError):
            TaskUpateSchemas(
                title="very long title " + "a" * 200,
                description="desc",
                is_complated=False,
            )


class TestTaskResponseSchemas:
    def test_valid_response(self):
        now = datetime.now()
        data = {
            "id": 1,
            "title": "Response Task",
            "description": "response desc",
            "is_complated": True,
            "created_date": now,
            "updated_date": now,
        }
        task_resp = TaskResponseSchemas(**data)
        assert task_resp.id == 1
        assert task_resp.created_date == now
        assert task_resp.updated_date == now

    def test_response_missing_required_fields(self):
        data = {
            "title": "Missing id",
            "description": "desc",
            "is_complated": False,
            "created_date": datetime.now(),
            "updated_date": datetime.now(),
        }
        with pytest.raises(ValidationError) as exc_info:
            TaskResponseSchemas(**data)
        errors = exc_info.value.errors()
        assert any(err["loc"][0] == "id" for err in errors)

    def test_response_wrong_datetime_type(self):
        data = {
            "id": 2,
            "title": "Wrong date",
            "description": "desc",
            "is_complated": False,
            "created_date": "not a datetime",
            "updated_date": datetime.now(),
        }
        with pytest.raises(ValidationError):
            TaskResponseSchemas(**data)

    def test_response_all_fields_inherited_from_base(self):
        with pytest.raises(ValidationError):
            TaskResponseSchemas(
                id=3,
                title="ab",
                description="desc",
                is_complated=True,
                created_date=datetime.now(),
                updated_date=datetime.now(),
            )