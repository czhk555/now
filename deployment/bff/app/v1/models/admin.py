from typing import List

from pydantic import Field

from deployment.bff.app.v1.models.helper import BaseRequestModel


class UpdateEmailsRequestModel(BaseRequestModel):
    user_emails: List[str] = Field(
        default=...,
        description='List of user emails who are allowed to access the flow',
    )
