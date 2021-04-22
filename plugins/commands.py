import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.pastebin import ezpaste

DELETE_DELAY = 6


async def _delay_delete_message(m: Message):
    await asyncio.sleep(DELETE_DELAY)
    await m.delete()


@Client.on_message(
    (filters.group | filters.private)
    & ~filters.edited
    & filters.regex('^\\/paste(@ezpastebot|)$')
)
async def paste(_, m: Message):
    reply = m.reply_to_message
    valid_input = reply and (reply.text or reply.document)
    if not valid_input:
        response = await m.reply_text(
            "Responder a un mensaje de texto/archivo con el comando de "
            "subir a [ezpaste](https://ezup.dev/p/)",
            quote=True,
            disable_web_page_preview=True
        )
        await _delay_delete_message(response)
        return
    url = await ezpaste(reply)
    if not url:
        await m.reply_text("Invalid", quote=True)
        return
    share_url = (
        f"https://t.me/share/url?url={url}"
        "&text=%E2%80%94%20__Pasted%20with__"
        "%20%F0%9F%A4%96%20%40ezpastebot"
    )
    await reply.reply_text(
        url,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Compartir",
                        url=share_url
                    ),
                    InlineKeyboardButton(
                        "Inline",
                        switch_inline_query=url
                    )
                ]
            ]
        ),
        quote=True
    )


@Client.on_message(filters.private
                   & filters.regex('^\\/start$')
                   & ~filters.edited)
async def start(_, m: Message):
    await m.reply_text(
        f"{emoji.LABEL} **Cómo utilizar este bot para subir el código a "
        "[ezpaste](https://ezup.dev/p)** "
        "(cualquiera de los siguientes métodos funciona):\n\n"
        "- Usa en modo inline\n"
        "- envia un texto o archivo de texto en privado\n"
        "- responder a un mensaje de texto o a un archivo de texto con /paste en privado "
        "o grupos (siéntase libre de añadir este bot a sus grupos, tiene "
        "el modo de privacidad activado para que no lea tu historial de chat\n\n"
        "Puedes cargar hasta 1 megabyte de texto en cada código\n\n",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Intenta inline",
                        switch_inline_query=""
                    )
                ]
            ]
        )
    )
