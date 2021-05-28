
def button(
        button_type: int,
        style,
        label,
        emoji,
        custom_id,
        url,
        disabled: bool
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
