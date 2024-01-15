"""Test telegram utils."""
from unittest.mock import AsyncMock, patch
from telegram import InlineKeyboardMarkup
import pytest
from src.tg_utils import field_reply


@pytest.mark.asyncio
async def test_field_reply():
    """Test field_reply functionality."""
    called_with = []

    async def mock_send_message(text, chat_id, reply_markup):
        called_with.append(text)

    with patch("src.tg_utils.generate_keyboard") as gen_key:
        gen_key.return_value = None
        context, update = AsyncMock(), AsyncMock()
        with pytest.raises(Exception):
            context.user_data = None
            await field_reply(update, context)
        context.user_data = AsyncMock()
        context.user_data['keyboard_state'].state = None
        with patch.object(InlineKeyboardMarkup, '__init__') as init_kb:
            init_kb.return_value = None
            context.application.bot.sendMessage = mock_send_message
            update.callback_query.message.chat.id = 42
            await field_reply(update, context, 'msg')
            assert called_with[-1] == 'msg'
            await field_reply(update, context, 'qwe')
            assert called_with[-1] == 'qwe'
