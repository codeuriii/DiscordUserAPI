# DiscordUserAPI

DiscordUserApi est un programme qui permet d'envoyer des messages automatiquement, sans utiliser le compte d'un bot, mais bien son compte utilisateur.
Si vous avez des idées ou des suggestions, voire des problèmes, je vous laisse aller voir la page [issues](https://github.com/codeuriii/DiscordUserAPI/issues).


---
# Version Requests:

### Initialisation et exemple:

```py
from discorduserapiVRequests import DiscordUserApi

dua = DiscordUserApi()

# First choice, login with your email-password
dua.login_mail("your mail", "your password")

# Or second choice, login with an oauth
dua.login_auth("your auth")

dua.send_msg('channel id', 'msg content')  # 200 (requests status code)
```

### Liste des compétences actuelles:

<details>
<summary>Envoyer un message</summary>

  **.send_msg()** - Le premier argument est l'identifiant du salon et le deuxième est le message en question.

  **int** _- Retourne le code de la requete_

</details>

<details>
<summary>Récupérer le profil d'un utilisateur</summary>

  **.get_profile()** - Le premier argument obligatoire est l'identifiant de l'utilisateur, et les autres sont si on veut récupérer les amis et/ou serveurs en commun.

  **dict** _- Retourne le profil sous la forme JSON_

</details>

<details>
<summary>Récupérer un certain nombre de messages dans un salon</summary>

  **.get_messages()** - Le premier argument est l'identifiant du salon, le second est le nombre de messages, fixé par défaut à 50.

  **list[dict]** _- Retourne les messages au format JSON (triés du plus récent au plus vieux)_

</details>

<details>
<summary>Récupérer le contenu d'un certain message</summary>

  **.get_content_in_single_msg()** - Le seul argument est le message, que l'on peut récupérer avec .get_messages(). Ne fonctionne qu'avec un seul message alors que .get_messages() retourne une liste.

  **str** _- Retourne le contenu au format str_

</details>


<details>
<summary>Récupérer le contenu d'une liste de messages</summary>

  **.get_content_in_multiple_msg()** - Le seul argument est la liste de message (par exemple .get_messages()).

  **list[str]** _- Retourne une liste des contenus des messages, dans l'ordre_

</details>

<details>
<summary>Jouer le son d'une notification Discord</summary>

  **.play_ping_sound()** - Joue le son d'une notification Discord.

  **None** _- Retourne rien_

</details>

<details>
<summary>Récupérer le lien de la vidéo de chargement de Discord</summary>

  **.get_link_discord_video_loading()** - Le lien de la vidéo.

  **str** _- Retourne le lien_

</details>

<details>
<summary>Récupérer le lien du son de la notification Discord</summary>

  **.get_link_ping()** - Le lien du son.

  **str** _- Retourne le lien_

</details>

<details>
<summary>Supprimer un ami</summary>

  **.delete_friend()** - Le seul argument est l'identifiant de l'utilisateur.

  **int** _- Retourne le statut de la requête_

</details>

<details>
<summary>Avoir la liste des amis</summary>

  **.get_friends()** - La liste de toutes les caractéristiques des amis.

  **list[dict]** _- Retourne les amis sous la forme d'une liste d'amis_

</details>

<details>
<summary>Avoir la liste des noms des amis</summary>

  **.get_friends_names()** - La liste des noms des amis.

  **list[str]** _- Retourne les noms des amis sous la forme d'une liste_

</details>

<details>
<summary>Avoir la liste des identifiants des amis</summary>

  **.get_friends_ids()** - La liste des identifiants des amis.

  **list[str]** _- Retourne les identifiants des amis sous la forme d'une liste_

</details>

<details>
<summary>Savoir si un utilisateur est un ami, grâce à son nom</summary>

  **.is_friend_by_name()** - Le seul argument est le nom de l'utilisateur en question.

  **bool** _- Retourne True si le nom d'utilisateur fait partie de tes amis, sinon retourne False_

</details>

<details>
<summary>Savoir si un utilisateur est un ami, grâce à son identifiant</summary>

  **.is_friend_by_name()** - Le seul argument est l'identifiant de l'utilisateur en question.

  **bool** _- Retourne True si l'identifiant de l'utilisateur fait partie de tes amis, sinon retourne False_

</details>

<details>
<summary>Avoir la liste de ses caractéristiques</summary>

  **.get_own_infos()** - Équivaut à faire un **.get_profile** avec son identifiant.

  **dict** _- Retourne l'ensemble des caractéristiques du compte avec lequel DiscordUserApi a été connecté_

</details>

<details>
<summary>Modifier le statut (online, offline)</summary>

  **.set_status()** - L'argument doit être dans la liste ['online', 'offline', 'inactive', 'notdistrub'].

  **int** _- Retourne le statut de la requête_

</details>

<details>
<summary>Bloquer un utilisateur, à partir de son identifiant</summary>

  **.block_user()** - L'argument est l'identifiant de l'utilisateur à bloquer.

  **int** _- Retourne le statut de la requête_

</details>

<details>
<summary>Débloquer un utilisateur, à partir de son identifiant</summary>

  **.unblock_user()** - L'argument est l'identifiant de l'utilisateur à débloquer.

  **int** _- Retourne le statut de la requête_

</details>

## Disclamer

DiscordUserApi est légal quand vous n'automatisez par entièrement un compte, ou que vous spammez. En l'utilisant, vous vous engagez a respecter les règles de Discord, et vous vous prettez au risque de bannir votre compte.

---
# Version Selenium:
Attention ! Je ne supporte plus la version Selenium.
Elle sera supprimée dans quelques jours le temps de vous adapter, et que je trouve le moyen de récupérer les amis en ligne avec les requètes.

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
