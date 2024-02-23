
import requests
import random
import pygame
from io import BytesIO
import json
import time
import threading

class DiscordUserAPI:

    def __init__(self, mail: str, password: str) -> None:
        self.mail = mail
        self.password = password
        self.login_infos = self.login()
        self.ouath = self.login_infos["token"]
        self.message_listeners = []
        self.is_listening = False
        self.headers_send_mdg = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": self.ouath,
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "prefer": "safe",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-super-properties": "please set your super properties"
        }
        self.headers_profile = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": self.ouath,
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "prefer": "safe",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-super-properties": "please set your super properties"
        }
        self.headers_messages = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": self.ouath,
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "prefer": "safe",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-super-properties": "please set your super properties"
        }
        self.username = self.get_profile(self.get_id())["user"]["username"]
        print("login successfuly")

    def login(self) -> dict:
        url = "https://discord.com/api/v9/auth/login"
        headers = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/json",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-fingerprint": "please set your finger print",
            "x-super-properties": "please set your super properties"
        }
        body = {
            "login": self.mail,
            "password": self.password,
            "undelete": False,
            "login_source": None,
            "gift_code_sku_id": None
        }

        response = requests.post(
            url,
            headers=headers,
            json=body
        )
        try:
            response.json()["token"]
            return response.json()
        except:
            raise ConnectionResetError(
                "Le service de ressources est soumis à une limitation de débit.\nVeuillez réessayer dans 5 secondes."
            )
    
    def get_id(self) -> str:
        return self.login_infos["user_id"]
    
    def send_msg(self, id_recv: str, msg_to_send: str) -> int:
        url = f"https://discord.com/api/v9/channels/{id_recv}/messages"

        body = {
            "mobile_network_type": "unknown",
            "content": msg_to_send,
            "nonce": ''.join([str(random.randrange(10)) for _ in range(19)]),
            "tts": False,
            "flags": 0
        }

        response = requests.post(
            url,
            headers=self.headers_send_mdg,
            json=body
        )

        return response.status_code
    
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
            headers=self.headers_profile
        )
        
        return response.json()

    
    def get_messages(self, channel_id: str, limit: str = "50") -> list[dict]:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}"
        
        response = requests.get(
            url,
            headers=self.headers_messages
        )

        return response.json()

    def get_avatar(self, profile: dict, size: str = "128") -> None:
        current_id = profile["user"]["id"]
        current_avatar = profile['user']['avatar']
        current_name = profile["user"]["username"] + ".png"

        url = f"https://cdn.discordapp.com/avatars/{current_id}/{current_avatar}.webp?size={size}"

        response = requests.get(url)

        with open(current_name, "wb") as f:
            f.write(response.content)

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

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "X-Context-Properties": "please set your context properties",
            "Authorization": self.ouath,
            "X-Super-Properties": "please set your super properties",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "please set your geolocalization",
            "X-Debug-Options": "bugReporterEnabled",
            "Alt-Used": "discord.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }

        referrer = "https://discord.com/channels/@me"
        params = {"referrer": referrer, "mode": "cors"}
        

        response = requests.delete(url,
            headers=headers,
            params=params
        )

        return response.status_code
    
    def add_friend(self, friend_name: str, discriminator: str = None) -> int:
        url = "https://discord.com/api/v9/users/@me/relationships"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json",
            "X-Context-Properties": "please set your context properties",
            "Authorization": self.ouath,
            "X-Super-Properties": "please set your super properties",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "please set your geolocalization",
            "X-Debug-Options": "bugReporterEnabled",
            "Alt-Used": "discord.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }
        data = {
            "username": friend_name,
            "discriminator": discriminator
        }

        response = requests.post(url, headers=headers, json=data)

        return response.status_code
    
    def get_friends(self) -> list[dict]:
        url = "https://discord.com/api/v9/users/@me/relationships"
        headers = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": self.ouath,
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "prefer": "safe",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-super-properties": "please set your super properties"
        }

        response = requests.get(url, headers=headers)

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
        headers = {
            "accept": "*/*",
            "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": self.ouath,
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "prefer": "safe",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-discord-timezone": "please set your geolocalization",
            "x-super-properties": "please set your super properties"
        }

        response = requests.get(url, headers=headers)

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
            headers = {
                "accept": "*/*",
                "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "authorization": self.ouath,
                "cache-control": "no-cache",
                "content-type": "application/json",
                "pragma": "no-cache",
                "prefer": "safe",
                "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "fr",
                "x-discord-timezone": "please set your geolocalization",
                "x-super-properties": "please set your super properties"
            }
            payload = "{\"settings\":\"x280\"}".replace("x280", all_status[status])
            response = requests.patch(url, headers=headers, data=payload)
            return response.status_code
        

    def block_user(self, user_id: str) -> int:

        url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json",
            "X-Context-Properties": "please set your context properties",
            "Authorization": self.ouath,
            "X-Super-Properties": "please set your super properties",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "please set your geolocalization",
            "X-Debug-Options": "bugReporterEnabled",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }
        payload = {
            "type": 2
        }

        response = requests.put(url, headers=headers, json=payload)

        return response.status_code
    
    def unblock_user(self, user_id: str) -> int:
        url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "X-Context-Properties": "please set your context properties",
            "Authorization": self.ouath,
            "X-Super-Properties": "please set your super properties",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "please set your geolocalization",
            "X-Debug-Options": "bugReporterEnabled",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }

        response = requests.delete(url, headers=headers)
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
