from enum import unique
from sqlmodel import Field, Relationship, SQLModel

import uuid


class License(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    token: str = Field(max_length=32, index=True, unique=True)
    value: bool


class LicenseCreate(License):
    pass


class LicenseUpdate(License):
    pass
