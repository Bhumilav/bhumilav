from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"🔐 𝘾𝙡𝙤𝙨𝙚"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🗨️ 𝐀𝐃𝐌𝐈𝐍 ↖️",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🤖 𝗔𝗨𝗧𝗛 💌",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔞 𝗕𝗟𝗔𝗖𝗞𝗟𝗜𝗦𝗧 🔞",
                    callback_data="help_callback hb3",
                ),

                InlineKeyboardButton(
                    text="💌 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 🔜",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔱 𝗚-𝗕𝗔𝗡 ♻️",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🔞 𝗟𝗬𝗥𝗜𝗖𝗦 🤖",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⛎ 𝗣𝗜𝗡𝗚 ⛎",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="🔽 𝗣𝗟𝗔𝗬 ⏹️",
                    callback_data="help_callback hb8",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📳 𝗣𝗟𝗔𝗬𝗟𝗜𝗦𝗧 ⏏️",
                    callback_data="help_callback hb6",
                ),

                InlineKeyboardButton(
                    text="🚳 𝗩𝗜𝗗𝗘𝗢𝗖𝗛𝗔𝗧𝗦 🚳",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="↖️ 𝗦𝗧𝗔𝗥𝗧 ↖️",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="🗨️ 𝗦𝗨𝗗𝗢 🔜",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"🔐 𝘾𝙡𝙤𝙨𝙚"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌸 𝗛𝗲𝗹𝗽 🌸",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
