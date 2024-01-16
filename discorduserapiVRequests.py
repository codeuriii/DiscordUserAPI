import json
import requests
import random
import pygame
from io import BytesIO

class DiscordUserAPI:

    def __init__(self, ouath) -> None:
        self.ouath = ouath
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
        self.headers_friends = {
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
    
    def send_msg(self, id_recv: str, msg_to_send: str):
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

        return response.text
    
    def get_link_ping(self):
        return 'https://discord.com/assets/7e95e417e6decf91459a.mp3'
    
    def get_link_discord_video_loading(self):
        return 'https://discord.com/assets/b85e9e5e26daee13304b.webm'
    
    def play_ping_sound(self):
        pygame.init()
        response = requests.get(self.get_link_ping())
        ping_mp3_data = BytesIO(response.content)
        pygame.mixer.music.load(ping_mp3_data)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def get_friends_online(self, legacy_name: bool = False, raw: bool = False):
        url = "https://discord.com/api/v9/users/839429032343765002/profile?with_mutual_friends_count=true"
        
        response = requests.get(
            url,
            headers=self.headers_friends
        )

        if raw:
            return response.json()
        elif legacy_name:
            return response.json()["legacy_username"]
        else:
            return response.json()["user"]["username"]

    
    def get_messages(self, channel_id: str, limit: str = "50", reverse_sort: bool = False):
        pass
