# DiscordUserAPI

DiscordUserApi si a program that allow you to send Discord message automatically without using a Discord bot account, but you’r own Discord account.
If you have a y idea’s or suggestion oreven probleme, you can always check the [issues](https://github.com/codeuriii/DiscordUserAPI/issues) pages.

---
# Selenium version:

### Initialiation and example:
```py
from discorduserapiVSelenium import DiscordUserApi

dua = DiscordUserApi()

dua.login('your username', 'your password')

dua.get_friends_online()  # ["friend 1", "friend 2", ...]
```

Send private messsage
> DUA can send a private message, with .send_dm() where the first argument is the ID of the salon, not the person, and the second is the message in question.

- Send a message in a server channel
> DUA can send a message to a salon, using .send_channel(), where the first argument is the server ID, the second is the salon ID, and the third is the message in question.

- Get online friends
> DUA can retrieve the list of online friends, with .get_friends_online() which takes no arguments and returns a list of the names of your online friends.

---
# Version Requests:

### Initialization and example:

```py
from discorduserapiVRequests import DiscordUserApi

dua = DiscordUserApi('your auth token')

dua.send_msg('channel id', 'msg content') # 200 (requests status code)
```

- Send a message
> DUA can send a message with .send_msg() where the first argument is the channel id and the second is the message in question.

**Warning: the oauth resets itself each time it reconnects!**