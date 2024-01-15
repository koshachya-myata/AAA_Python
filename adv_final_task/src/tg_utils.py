"""Utils for tg keyboard and reply functionality."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


def generate_keyboard(state: list[list[str]]) ->\
                                            list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyboard 3x3 (telegram buttons)."""
    return [
        [
            InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
            for r in range(3)
        ]
        for c in range(3)
    ]


async def field_reply(update: Update,
                      context: ContextTypes.DEFAULT_TYPE,
                      msg: str):
    """Reply and send keyboard with tictactoe field."""
    if context.user_data is None:
        raise Exception('Bad parameters of Context user data.')
    keyboard = generate_keyboard(
        context.user_data['keyboard_state'].get_state()
        )
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query is None or update.callback_query.message is None:
        raise Exception('Bad parameters of Update callback_query.')
    await context.application.bot.sendMessage(
            text=msg,
            chat_id=update.callback_query.message.chat.id,
            reply_markup=reply_markup,
        )
