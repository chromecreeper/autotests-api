import uuid
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic import BaseModel, Field

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
        title: str
        maxScore: int
        minScore: int
        description: str
        estimatedTime: str
        previewFileId: str
        createdByUserId: str

class CreateCourseResponseSchema(BaseModel):
        """
        Описание структуры ответа создания курса.
        """
        course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
        """
        Описание структуры запроса на обновление курса.
        """
        title: str | None = None
        maxScore: int | None = None
        minScore: int | None = None
        description: str | None = None
        estimatedTime: str | None = None
