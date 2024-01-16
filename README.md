# DiscordUserAPI

DiscordUserApi est un programme qui permet d'envoyer des messages automatiquement, sans utiliser le compte d'un bot, mais bien son compte utilisateur.
Si vous avez des idées ou des suggestions, voire des problèmes, je vous laisse aller voir la page [issues](https://github.com/codeuriii/DiscordUserAPI/issues).


---
# Version Requests:

### Initialisation et exemple:

```py
from discorduserapiVRequests import DiscordUserApi

dua = DiscordUserApi('your auth token')

dua.send_msg('channel id', 'msg content')  # 200 (requests status code)
```
**Attention, l'oauth se reset a chaque reconenction !**

### Liste des compétences actuelles:

- Envoyer un message

.send_msg() - Le premier argument est l'identifiant du salon et le deuxième est le message en question.
**int** _- Retourne le code de la requete_

- Récuperer le profil d'un utilisateur
> .get_profile() - Le permier argument obligatoire est l'identifiant de l'utilisateur, et les autres sont si on veut récupérer les amis et/ou serveurs en commun.
>
> **dict** _- Retourne le profil sous la forme json_

- Récupérer un certain nombre de message dans un salon
> .get_messages() - Le premier argument est l'identifiant du salon, le second est le nombre de messages, fixé par defaut a 50
>
> **list[dict]** _- Retourne les messages au format json (triés du plus récent au plus vieux)_

- Récupérer le contenu d'un certain message
> .get_content_in_single_msg() - Le seul argument est le message, que l'on peut récupérer avec .get_messages(). ne fonctionne qu'avec un seul message alors que .get_messages() retourne une liste.
>
> **str** _- Retourne le contenu au format str_

- Récupérer le contenu d'une liste de messages
> .get_content_in_multiple_msg() - Le seul argument est la liste de message, (par exemple .get_messages())
>
> **list[str]** _- Retourne une liste des contenus des messages, dans l'ordre_

- Jouer le son d'une notification discord
> .play_ping_sound() - Joue le son d'une notification discord
>
> **None** _- Retourne rien_

- Récupérer le lien de la vidéo de chargement de discord
> .get_link_discord_video_loading() - Le lien de la vidéo
>
> **str** _- Retourne le lien_

- Récupérer le lien du son de la notification de discord
> .get_link_ping() - Le lien du son
>
> **str** _- Retourne le lien_


---
# Version Selenium:
Attention ! Je ne supporte plus la version Selenium
Elle sera supprimée dans quelques jours le temps de vous adapter.

### Initialisation et exemple:
```py
from discorduserapiVSelenium import DiscordUserApi

dua = DiscordUserApi()

dua.login('your username', 'your password')

dua.get_friends_online()  # ["friend 1", "friend 2", ...]
```

### Liste des compétences actuelles :

- Envoyer un message privé
> DUA peut envoyer un message privé, avec .send_dm() ou le premier argument est l'identifiant du salon, et pas de la personne attention, et le second est le message en question.

- Envoyer un message dans un channel de serveur
> DUA peut envoyer un message dans un salon, avec .send_channel() ou le premier argument est l'identifiant du serveur, le second est l'identifiant du salon, et le troisième est le message en question.

- Récupérer les amis en lignes
> DUA peut récupérer la liste des amis en lignes, avec .get_friends_online() qui ne prend pas d'argument et retourne une liste des noms de vos amis en lignes.
