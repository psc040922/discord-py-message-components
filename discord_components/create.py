from typing import Union

class ComponentType:

    @property
    def action_row(self):
        return 1

    @property
    def button(self):
        return 2


class ButtonStyle:

    @property
    def primary(self):
        return 1

    @property
    def secondary(self):
        return 2

    @property
    def success(self):
        return 3

    @property
    def danger(self):
        return 4

    @property
    def link(self):
        return 5


def button(
        button_type: Union[int, ComponentType],
        style: Union[int, ButtonStyle],
        label: str,
        custom_id: str,
        emoji: dict = None,
        url: str = None,
        disabled: bool = False
) -> dict:
    data = {
        "type": button_type,
        "style": style,
        "label": label,
        "emoji": emoji,
        "custom_id": custom_id,
        "url": url,
        "disabled": disabled
    }
    return data
