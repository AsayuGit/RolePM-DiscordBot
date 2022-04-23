 Ce bot permet d'envoyer un message privé a tout les membres d'un role.
 Cela facilite la publication d'annonces.

Il supporte 3 commandes:
!help : Décrit toute les commandes existantes
!ping : Répond pong (util pour vérifier le bon fonctionnement du bot)
!message [role] [message] : Envoie le message privé a tout les membre du role

Utilisation : python main.py -c config.cfg [OPTIONS]
-v active les logs

Il est nécessaire de renseigner le token de votre bot discord dans le fichier
config.cfg sous la forme TOKEN=key

structure du code:
main.py      : Parsing des arguments et initialisation du bot et ses dépendences
MyBot.py     : Implémentation de la class du bot
BotLogger.py : Implémentation de la class du logger
config.cfg   : Fichier de config contenant le token du bot.
