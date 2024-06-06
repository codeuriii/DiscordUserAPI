
import requests
import random
import pygame
from io import BytesIO
import json
import time
import threading
import discord as ds

class DiscordUserAPI:

    def __init__(self) -> None:
        self.message_listeners = []
        self.is_listening = False

    def login_oauth(self, ouath: str):
        self.ouath = ouath
        self.headers = {
            "authorization": self.ouath,
        }

    def login_mail(self, mail: str, password: str) -> dict:
        url = "https://discord.com/api/v9/auth/login"
        body = {
            "login": mail,
            "password": password,
        }

        response = requests.post(
            url,
            json=body
        )
        try:
            self.ouath = response.json()["token"]
            self.headers = {
                "authorization": self.ouath,
            }
            self.login_infos = response.json()
        except:
            raise ConnectionResetError(
                "La requète renvoie un captcha.\nVeuillez arrêter de spammer le /v9/auth/login.\nVeuillez utiliser le login par oauth."
            )
    
    def get_id(self) -> str:
        return self.login_infos["user_id"]
    
    def send_msg(self, id_recv: str, msg_to_send: str) -> dict[str, (str | int | dict | list | bool | None)]:
        url = f"https://discord.com/api/v9/channels/{id_recv}/messages"

        body = {
            "content": msg_to_send,
            "nonce": ''.join([str(random.randrange(10)) for _ in range(19)]),
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=body
        )

        return response.json()
    
    def send_embed(self, id_recv: str, embed: ds.Embed):
        print("WARNING: function is not functional")
        return
    
        url = f"https://discord.com/api/v9/channels/{id_recv}/messages"

        body = {
            "embeds": [embed.to_dict()],
            "content": None,
            "components": [],
            "tts": False,
            "nonce": ''.join([str(random.randrange(10)) for _ in range(19)]),
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=body
        )

        return response.text

    def get_bots(self, guild_id: str):
        return self.get_commands(guild_id).get("applications", [])
    
    def get_commands(self, guild_id: str):
        url = f"https://discord.com/api/v9/guilds/{guild_id}/application-command-index"
        
        response = requests.get(
            url,
            headers=self.headers
        )
        return response.json()

    def use_command(self, channel_id: str, guild_id: str, name: str):

        commands = self.get_commands(guild_id)

        for command in commands.get("application_commands"):
            if command.get("name", "") == name:
                interaction = command
                break

        body = {
            "type": 2,
            "application_id": interaction["application_id"],
            "guild_id": guild_id,
            "channel_id": channel_id,
            "session_id": "idk for now",
            "data": {
                "version": interaction["version"],
                "id": interaction["id"],
                "name": interaction["name"],
                "type": interaction["type"],
                "options": interaction["options"],
                "application_command": {
                    "id": interaction["id"],
                    "type": interaction["id"],
                    "application_id": interaction["application_id"],
                    "version": interaction["version"],
                    "name": interaction["name"],
                    "description": interaction["description"],
                    "dm_permission": interaction["dm_permission"],
                    "integration_types": interaction["integration_types"],
                    "global_popularity_rank": interaction.get("global_popularity_rank", 0),
                    "options": interaction["options"],
                    "description_localized": interaction["description"],
                    "name_localized": interaction["name"]
                },
                "attachments": []
            },
            "nonce": ''.join([str(random.randrange(10)) for _ in range(19)]),
            "analytics_location": "slash_ui"
        }
        response = requests.post("https://discord.com/api/v9/interactions",
            headers=self.headers,
            json=body,
        )
        return response
    
    def get_opened_mps(self):
        url = "https://discord.com/api/v9/users/@me/affinities/users"

        response = requests.get(url, headers=self.headers)

        result = []
        for user in response.json().get("user_affinities", []):
            if user["user_id"] != 0:
                result.append(user["user_id"])

        return result

    def get_connections(self):
        url = "https://discord.com/api/v9/users/@me/connections"

        response = requests.get(url, headers=self.headers)
        result = response.json()
        result.pop(0)

        return result

    def get_link_ping(self) -> str:
        return 'https://discord.com/assets/7e95e417e6decf91459a.mp3'
    
    def get_link_discord_video_loading(self) -> str:
        return 'https://discord.com/assets/b85e9e5e26daee13304b.webm'
    
    def play_ping_sound(self) -> None:
        pygame.init()
        response = requests.get(self.get_link_ping())
        ping_mp3_data = BytesIO(response.content)
        pygame.mixer.music.load(ping_mp3_data)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def get_profile(self, user_id: str) -> dict:
        url = f"https://discord.com/api/v9/users/{user_id}/profile"

        response = requests.get(
            url,
            headers=self.headers
        )
        return response.json()

    
    def get_messages(self, channel_id: str, limit: str = "50") -> list[dict]:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}"
        
        response = requests.get(
            url,
            headers=self.headers
        )

        return response.json()

    def get_avatar(self, user_id: str, size: str = "128") -> bytes:
        profile = self.get_profile(user_id)
        current_id = profile["user"]["id"]
        current_avatar = profile['user']['avatar']

        url = f"https://cdn.discordapp.com/avatars/{current_id}/{current_avatar}.webp?size={size}"

        response = requests.get(url)

        return response.content

    def get_content_in_single_msg(self, msg) -> str:
        if type(msg) == list and len(msg) == 1:
            print("WARNING - msg is a list, not a dict")
            return msg[0]["content"]
        elif type(msg) == dict:
            return msg["content"]
        else:
            raise TypeError(
                "Cannot get content: msg is not a dict"
            )
    
    def get_content_in_multiple_msg(self, msgs: list[dict]) -> list[str]:
        l = []

        for msg in msgs:
            l.append(self.get_content_in_single_msg(msg))

        return l
    
    def delete_friend(self, friend_id: str) -> int:
        url = f"https://discord.com/api/v9/users/@me/relationships/{friend_id}"

        referrer = "https://discord.com/channels/@me"
        params = {"referrer": referrer, "mode": "cors"}
        
        response = requests.delete(url,
            headers=self.headers,
            params=params
        )

        return response.status_code
    
    def get_friends(self) -> list[dict]:
        url = "https://discord.com/api/v9/users/@me/relationships"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_friends_names(self) -> list[str]:
        friends = self.get_friends()
        f = []

        for friend in friends:
            f.append(friend["user"]["username"])
        return f
    
    def get_friends_ids(self) -> list[str]:
        friends = self.get_friends()
        f = []

        for friend in friends:
            f.append(friend["id"])
        return f

    def is_friend_by_name(self, username: str) -> bool:
        friends_names = self.get_friends_names()

        if username.lower() in map(str.lower, friends_names):
            return True
        return False
    
    def is_friend_by_id(self, id: str) -> bool:
        friends_ids = self.get_friends_ids()

        if id in friends_ids:
            return True
        return False
    
    def get_own_infos(self) -> dict:
        url = "https://discord.com/api/v9/users/@me"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def set_status(self, status: str) -> int:
        """
        The status can only be in this list: ["online", "offline", "inactive", "notdistrub"].
        """
        status_possibles = ["online", "offline", "inactive", "notdistrub"]
        if not status in status_possibles:
            raise ValueError(
                'The status can only be in this list: ["online", "offline", "inactive", "notdistrub"].'
            )
        else:
            with open("status.json", 'r') as f:
                all_status = json.load(f)

            url = "https://discord.com/api/v9/users/@me/settings-proto/1"
            payload = "{\"settings\":\"x280\"}".replace("x280", all_status[status])
            response = requests.patch(url, headers=self.headers, data=payload)
            return response.status_code
        

    def block_user(self, user_id: str) -> int:

        url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
        payload = {
            "type": 2
        }

        response = requests.put(url, headers=self.headers, json=payload)
        return response.status_code
    
    def unblock_user(self, user_id: str) -> int:
        url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code

    def add_message_listener(self, listener_func):
        self.message_listeners.append(listener_func)

    def start_listening(self, channel_id: str):
        if not self.is_listening:
            self.is_listening = True
            self.xblorg = channel_id
            listener_thread = threading.Thread(target=self._listen_for_messages)
            listener_thread.daemon = True
            listener_thread.start()

    def _listen_for_messages(self):
        svgd = self.get_messages(self.xblorg, "1")
        while self.is_listening:
            latest_message = self.get_messages(self.xblorg, "1")
            if svgd != latest_message:
                svgd = latest_message
                self._notify_message_listeners(latest_message)
            time.sleep(1)

    def _notify_message_listeners(self, message):
        for listener_func in self.message_listeners:
            listener_func(message)
