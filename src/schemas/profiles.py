from datetime import date
from typing import Optional

from fastapi import UploadFile, Form, File, HTTPException, status
from pydantic import BaseModel, field_validator

from validation.profile import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date,
    validate_info
)


class ProfileSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: Optional[str] = None

    @field_validator("first_name", "last_name", mode="before")
    @classmethod
    def validate_names(cls, value):
        try:
            validate_name(value)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(e)
            )
        return value.lower()

    @field_validator("gender", mode="before")
    @classmethod
    def validate_field_gender(cls, value):
        try:
            validate_gender(value)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(e)
            )
        return value

    @field_validator("date_of_birth", mode="before")
    @classmethod
    def validate_date_of_birth(cls, value):
        try:
            validate_birth_date(value)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(e)
            )
        return value

    @field_validator("info", mode="before")
    @classmethod
    def validate_avatar(cls, value):
        return validate_image(value)
    def validate_info(cls, value):
        try:
            validate_info(value)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(e)
            )
        return value

