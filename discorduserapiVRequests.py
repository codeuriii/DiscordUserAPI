
import requests
import random
import pygame
from io import BytesIO


class DiscordUserAPI:

    def __init__(self, mail: str, password: str) -> None:
        self.username = mail
        self.password = password
        self.ouath = self.get_token()
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
            "x-discord-timezone": "Indian/Reunion",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vcGFsYWRpdW0tcHZwLmZyLyIsInJlZmVycmluZ19kb21haW4iOiJwYWxhZGl1bS1wdnAuZnIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9sb2dpbiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5MDQ4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
            "x-discord-timezone": "Indian/Reunion",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vcGFsYWRpdW0tcHZwLmZyLyIsInJlZmVycmluZ19kb21haW4iOiJwYWxhZGl1bS1wdnAuZnIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9sb2dpbiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5MDQ4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
            "x-discord-timezone": "Indian/Reunion",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vcGFsYWRpdW0tcHZwLmZyLyIsInJlZmVycmluZ19kb21haW4iOiJwYWxhZGl1bS1wdnAuZnIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9sb2dpbiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5MDQ4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }

    def get_token(self) -> str:
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
            "x-discord-timezone": "Asia/Dubai",
            "x-fingerprint": "1197033163386523658.rQaK2nwJRlDG0aBEYsZ5mt1uWpc",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5MDQ4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"
        }
        body = {
            "login": self.username,
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

        return response.json()["token"]
    
    def get_id(self) -> str:
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
            "x-discord-timezone": "Asia/Dubai",
            "x-fingerprint": "1197033163386523658.rQaK2nwJRlDG0aBEYsZ5mt1uWpc",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5MDQ4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"
        }
        body = {
            "login": self.username,
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

        return response.json()["user_id"]
    
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
        current_name = profile["user"]["global_name"] + ".png"

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
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IkZyaWVuZHMifQ==",
            "Authorization": self.ouath,
            "X-Super-Properties": "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZnIiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6MTIxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTIxLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjEuMCIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5NTAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "Indian/Reunion",
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
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
            "Authorization": self.ouath,
            "X-Super-Properties": "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZnIiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6MTIxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTIxLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjEuMCIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5NTAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "Indian/Reunion",
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
            "x-discord-timezone": "Indian/Reunion",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjAuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vcGFsYWRpdW0tcHZwLmZyLyIsInJlZmVycmluZ19kb21haW4iOiJwYWxhZGl1bS1wdnAuZnIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9sb2dpbiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU5NTAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }

        response = requests.get(url, headers=headers)

        return response.json()
    
    def get_friends_names(self) -> list[str]:
        friends = self.get_friends()
        f = []

        for friend in friends:
            f.append(friend["user"]["global_name"])

        return f

    def is_friend(self, user_id: str) -> bool:
        pass