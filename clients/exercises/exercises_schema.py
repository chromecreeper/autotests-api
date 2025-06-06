import uuid

from pydantic import BaseModel, Field

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    courseId: str
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    order_index: int = Field(alias="orderIndex", default=0)
    description: str
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание данных задания
    """
    title: str
    courseId: str
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    order_index: int = Field(alias="orderIndex", default=0)
    description: str
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление данных задания
    """
    title: str | None
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    order_index: int = Field(alias="orderIndex", default=0)
    description: str | None
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
