from pydantic import BaseModel, EmailStr, constr, Field

class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """Модель запроса на создание пользователя"""
    email: EmailStr
    password: constr(min_length=1)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Модель ответа с данными созданного пользователя"""
    user: UserSchema