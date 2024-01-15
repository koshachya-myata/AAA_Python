"""Game states async functions for tictactoe tg bot."""
from src.tictactoe_utils import TicTacToeField
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler
from src.tg_utils import generate_keyboard, field_reply
from config import CONTINUE_GAME, FINISH_GAME


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    if context.user_data is None:
        raise Exception('Bad Context User data')
    if update.message is None:
        raise Exception('Bad Update message info')
    context.user_data['keyboard_state'] = TicTacToeField()
    keyboard = generate_keyboard(
        context.user_data['keyboard_state'].get_state()
        )
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.\
        reply_text('X (your) turn! Please, put X to the free place',
                   reply_markup=reply_markup)
    return CONTINUE_GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Do main processing of the game."""
    async def process_draw():
        if context.user_data['keyboard_state'].is_draw():
            await field_reply(update, context, 'Oh-oh-oh. Its draw!')
            return True
        return False

    if context.user_data is None:
        raise Exception('Bad parameters of Context user data.')
    query = update.callback_query
    if query is None or query.data is None:
        raise Exception('Bad CallbackQuery info.')
    await query.answer()
    pos = tuple(map(int, list(query.data)))
    is_win = context.user_data['keyboard_state'].place_figure(pos)
    if is_win:
        await field_reply(update, context, 'Congratulations! You won.')
        return FINISH_GAME
    if await process_draw():
        return FINISH_GAME
    is_win = context.user_data['keyboard_state'].ai_move()
    if is_win:
        await field_reply(update, context, 'Unfortunately you lost...')
        return FINISH_GAME
    if await process_draw():
        return FINISH_GAME
    await field_reply(update, context, 'Next move!')
    return CONTINUE_GAME


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Return `ConversationHandler.END`.

    Which tells the ConversationHandler that the conversation is over.
    """
    # reset state to default so you can play again with /start
    if context.user_data is None:
        raise Exception('Bad parameters of Context user data.')
    context.user_data['keyboard_state'] = TicTacToeField()
    return ConversationHandler.END
