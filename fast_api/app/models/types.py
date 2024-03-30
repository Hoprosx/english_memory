from typing import Annotated

from sqlalchemy.orm import mapped_column

primary_key = Annotated[int, mapped_column(primary_key=True)]
