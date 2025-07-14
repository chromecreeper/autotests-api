import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema, UpdateExerciseRequestSchema
from tools.routes import APIRoutes

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод для получение списка заданий определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES,
                        params=query.model_dump(by_alias=True)
                        )

    @allure.step("Get exercise")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES,
                         json=request.model_dump(by_alias=True)
                         )

    @allure.step("Update exercise")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}",
                          json=request.model_dump(by_alias=True)
                          )

    @allure.step("Delete exercise")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
