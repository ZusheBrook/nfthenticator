import dataclasses


@dataclasses.dataclass(init=True)
class User:
    user_name: str
    user_id: str
    email: str

