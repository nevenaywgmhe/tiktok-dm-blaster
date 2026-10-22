from dataclasses import dataclass
from string import Template


@dataclass
class MessageTemplate:
    raw: str

    def render(self, username: str) -> str:
        return Template(self.raw).safe_substitute(username=username, user=username)
</Parameter>