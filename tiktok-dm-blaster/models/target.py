from dataclasses import dataclass


@dataclass
class Target:
    username: str
    user_id: str | None = None
    verified: bool = False
    can_dm: bool = True

    @classmethod
    def from_line(cls, line: str) -> "Target":
        parts = line.split(",")
        return cls(
            username=parts[0].strip().lstrip("@"),
            user_id=parts[1].strip() if len(parts) > 1 else None,
        )