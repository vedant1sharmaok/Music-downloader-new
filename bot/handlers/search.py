from pyrogram import filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

def inline_search_handler(app):
    @app.on_inline_query()
    async def inline(client, inline_query: InlineQuery):
        results = [
            InlineQueryResultArticle(
                title="Example result",
                input_message_content=InputTextMessageContent("You selected: Example"),
                description="A sample inline search result",
            )
        ]
        await inline_query.answer(results, cache_time=1)
