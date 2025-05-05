from datetime import date
from typing import Optional

from fastapi import UploadFile, Form, File, HTTPException
from pydantic import BaseModel, field_validator, HttpUrl

from validation.profile import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date
)


class ProfileSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: Optional[str] = None
    avatar: UploadFile

    @field_validator("first_name", "last_name", mode="before")
    @classmethod
    def validate_names(cls, value):
        return validate_name(value)

    @field_validator("gender", mode="before")
    @classmethod
    def validate_field_gender(cls, value):
        return validate_gender(value)

    @field_validator("date_of_birth", mode="before")
    @classmethod
    def validate_date_of_birth(cls, value):
        return validate_birth_date(value)

    @field_validator("avatar", mode="before")
    @classmethod
    def validate_avatar(cls, value):
        return validate_image(value)
