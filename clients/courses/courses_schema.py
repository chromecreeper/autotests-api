import uuid
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание модели курса.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

class GetCoursesQuerySchema(BaseModel):
        """
        Описание структуры запроса на получение списка курсов.
        """
        userId: str

class CreateCourseRequestSchema(BaseModel):
        """
        Описание структуры запроса на создание курса.
        """
        title: str = Field(default_factory=fake.sentence)
        max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
        min_score: int = Field(alias="minScore", default_factory=fake.min_score)
        description: str = Field(default_factory=fake.text)
        estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
        preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
        created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class CreateCourseResponseSchema(BaseModel):
        """
        Описание структуры ответа создания курса.
        """
        course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
        """
        Описание структуры запроса на обновление курса.
        """
        title: str | None = Field(default_factory=fake.sentence)
        max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
        min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
        description: str | None = Field(default_factory=fake.text)
        estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
