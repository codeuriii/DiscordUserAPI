# DiscordUserAPI

DiscordUserApi est un programme qui permet d'envoyer des messages automatiquement, sans utiliser le compte d'un bot.

Liste des compétences :

- Envoyer un message privé
DUA peut envoyer un message privé, avec .send_dm() ou le premier argument est l'identifiant du salon, et pas de la personne attention, et le second est le message en question.

- Envoyer un message dans un channel de serveur
DUA peut envoyer un message dans un salon, avec .send_channel() ou le premier argument est l'identifiant du serveur, le second est l'identifiant du salon, et le troisième est le message en question.

- Récupérer les amis en lignes
DUA peut récupérer la liste des amis en lignes, avec .get_friends_online() qui ne prend pas d'argument et retourne une liste des noms de vos amis en lignes.

/!\ Je commence a abandonner Selenium pour me trouner vers requests.