# DiscordUserAPI

DiscordUserApi est un programme qui permet d'envoyer des messages automatiquement, sans utiliser le compte d'un bot, mais bien son compte utilisateur.
Si vous avez des idées ou des suggestions, voire des problèmes, je vous laisse aller voir la page [issues](https://github.com/codeuriii/DiscordUserAPI/issues).

---
# Version Selenium:

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
> .send_msg() - Le premier argument est l'identifiant du salon et le deuxième est le message en question.
> *Retourne le code de la requete*

- Récuperer le profil d'un utilisateur
> .get_profile() - Le permier argument obligatoire est l'identifiant de l'utilisateur, et les autres sont si on veut récupérer les amis et/ou serveurs en commun.
> *Retourne le profil sous la forme json*

- Récupérer un certain nombre de message dans un salon
> .get_messages() 

