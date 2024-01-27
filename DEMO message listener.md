Pour utiliser le listener de message, suivez ces instructions

1. Pour commencer, créez la fonction qui sera appellée quand un nouveau message sera envoyé
```py
def mafonction(msg):
    print(msg)
```

2. Ensuite ajouter la fonction a la liste des fonctions appelées au nouveau message
```py
DUA.add_message_listener(mafonction)
```

3. Pour terminer, démarrez le listener
```py
DUA.start_listener("l'identifiant du salon duquel vous voulez surveiller les messages")
```