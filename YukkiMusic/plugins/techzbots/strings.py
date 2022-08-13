from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
🧘‍♀️ **ʜʏ  MENTION **

**ɪ ᴀ ᴍ ᴠɪʙᴇs ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ 

🍷 **🍷⭐【🇸  𝗨 𝗣 𝗣 𝗢 𝗥 𝗧 】⭐🍷

█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ 【⚡ @TAMIL_CHATBOX ⚡】 █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ 【⚡ @TAMIL_CHATFUN ⚡】 █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█**
"""

COMMANDS_TEXT = f"""
✨ **ʜᴇʟʟᴏ MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 ᴄ ᴏ ᴍ ᴍ ᴀ ɴ ᴅ s", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 s ᴇ ᴛ ᴛ ɪ ɴ ɢ s", callback_data="settings_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ᴜ ᴘ ᴅ ᴀ ᴛ ᴇ Channel", url="https://t.me/king_bioz"
            ),
            InlineKeyboardButton(
                text="s ᴜ ᴘ ᴘ ᴏ ʀ ᴛ Group", url="https://t.me/Tamil_chatbox"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🍷 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🍷", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text=" ᴄ ᴏ ᴍ ᴍ ᴀ ɴ ᴅ s", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="ᴄ ʜ ᴀ ɴ ɴ ᴇ ʟ", url="https://t.me/king_bioz"
            ),
            InlineKeyboardButton(
                text="s ᴜ ᴘ ᴘ ᴏ ʀ ᴛ", url="https://t.me/Tamil_chatbox"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ᴀᴅᴍɪɴ Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="ʙᴏᴛ Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴘʟᴀʏ Commands", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="ᴇxᴛʀᴀ Commands", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ᴀᴅᴍɪɴ Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="ʙᴏᴛ Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴘʟᴀʏ Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="sᴜᴅᴏ Commands", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴇxᴛʀᴀ Commands", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="sᴜᴅᴏ Commands", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅--**Admin Commands:**--

c stands for channel play.

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.

✅--**Specific Skip:**--
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅--**Loop Play:**--
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

"""
AUTH_TEXT = """
✅--**Auth Users:**--
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**Bot Commands:**--

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Yukki Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
✅--**Play Commands:**--

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

c stands for channel play.
v stands for video play.
force stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✅--**Bot's Server Playlists:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""


BASIC_TEXT = """
💠 **Basic Commands:**

/start - Start the bot

/help - Get help message

/play - Play songs or videos in vc

/vplay - Play video in VC

/settings - Check Settings of bot in your group

**Some Useful Commands :** 

/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Auth Commands", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 ʙᴀsɪᴄ Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="🍷 ᴀᴅᴠᴀɴᴄᴇᴅ Commands", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ ʙ ᴀ ᴄ ᴋ", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 ᴄ ʟ ᴏ s ᴇ ", callback_data="close_btn"
            ),            
        ],                        
    ]
)
