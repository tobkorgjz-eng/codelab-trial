"""Render an example chat card as HTML."""

from html import escape

CAPTION = "Example chat with example data"


def render_chat_card(helper_name, you_text, bot_text):
    """Return HTML for an example chat card.

    Every piece of text is HTML-escaped (including quotes).
    Raises ValueError if bot_text is empty or only whitespace.
    """
    if not bot_text or not str(bot_text).strip():
        raise ValueError("bot_text must not be empty")

    name = escape(str(helper_name), quote=True)
    you = escape(str(you_text), quote=True)
    bot = escape(str(bot_text), quote=True)
    caption = escape(CAPTION, quote=True)

    return (
        '<figure class="hp-chat">\n'
        '  <div class="hp-chat-bubble hp-chat-you">\n'
        '    <span class="hp-chat-name">You</span>\n'
        f'    <p>{you}</p>\n'
        '  </div>\n'
        '  <div class="hp-chat-bubble hp-chat-bot">\n'
        f'    <span class="hp-chat-name">{name}</span>\n'
        f'    <p>{bot}</p>\n'
        '  </div>\n'
        f'  <figcaption>{caption}</figcaption>\n'
        '</figure>'
    )
