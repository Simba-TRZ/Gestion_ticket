import json

# Dictionnaire pour stocker les tickets
tickets = {}

# Fonction pour créer un ticket
def creer_ticket(description, priorite):
    for ticket in tickets.values():
        if ticket["description"] == description:
            print(f"Un ticket avec la description '{description}' existe déjà.")
            return
    ticket_id = max(tickets.keys(), default=0) + 1
    tickets[ticket_id] = {"description": description, "statut": "Ouvert", "priorite": priorite}
    print(f"Le ticket #{ticket_id} a été créé avec succès : {description} (Priorité : {priorite})")

# Fonction pour afficher tous les tickets
def afficher_tickets():
    if not tickets:
        print("Il n'y a aucun ticket pour le moment.")
    else:
        print("Voici les tickets actuels :")
        for ticket_id, details in tickets.items():
            print(f"Ticket #{ticket_id}: {details['description']} - Statut: {details['statut']} - Priorité: {details.get('priorite', 'Non définie')}")

# Fonction pour mettre à jour le statut d'un ticket
def mettre_a_jour_statut(ticket_id, nouveau_statut):
    if ticket_id in tickets:
        tickets[ticket_id]['statut'] = nouveau_statut
        print(f"Le ticket #{ticket_id} a été mis à jour. Nouveau statut : {nouveau_statut}")
    else:
        print(f"Le ticket #{ticket_id} n'existe pas. Impossible de le mettre à jour.")

# Fonction pour supprimer un ticket
def supprimer_ticket(ticket_id):
    if ticket_id in tickets:
        del tickets[ticket_id]
        print(f"Le ticket #{ticket_id} a été supprimé.")
    else:
        print(f"Le ticket #{ticket_id} n'existe pas.")

# Fonction pour sauvegarder les tickets dans un fichier
def sauvegarder_tickets(fichier):
    with open(fichier, 'w') as f:
        json.dump(tickets, f)
    print(f"Les tickets ont été sauvegardés dans le fichier {fichier}.")

# Fonction pour charger les tickets à partir d'un fichier
def charger_tickets(fichier):
    global tickets
    try:
        with open(fichier, 'r') as f:
            tickets = json.load(f)
        tickets = {int(k): v for k, v in tickets.items()}  # Convertir les clés en entiers
        print(f"Les tickets ont été chargés depuis le fichier {fichier}.")
    except FileNotFoundError:
        print(f"Aucun fichier {fichier} trouvé. Aucun ticket chargé.")

# Fonction pour rechercher un ticket par mot-clé
def rechercher_ticket(critere):
    resultats = {id: details for id, details in tickets.items() if critere.lower() in details["description"].lower()}
    if resultats:
        print("Tickets trouvés :")
        for ticket_id, details in resultats.items():
            print(f"Ticket #{ticket_id}: {details['description']} - Statut: {details['statut']} - Priorité: {details.get('priorite', 'Non définie')}")
    else:
        print(f"Aucun ticket ne correspond au critère : {critere}")

# Fonction pour exporter les tickets dans un fichier texte
def exporter_tickets(fichier):
    with open(fichier, 'w') as f:
        for ticket_id, details in tickets.items():
            f.write(f"Ticket #{ticket_id}: {details['description']} - Statut: {details['statut']} - Priorité: {details.get('priorite', 'Non définie')}\n")
    print(f"Les tickets ont été exportés dans le fichier {fichier}.")

# Charger les tickets depuis le fichier au démarrage
charger_tickets('tickets.json')

# Menu interactif
while True:
    print("\nMenu :")
    print("1. Créer un ticket")
    print("2. Afficher tous les tickets")
    print("3. Mettre à jour le statut d'un ticket")
    print("4. Supprimer un ticket")
    print("5. Sauvegarder les tickets")
    print("6. Quitter")
    print("7. Rechercher un ticket")
    print("8. Exporter les tickets en fichier texte")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        description = input("Entrez la description du ticket : ")
        priorite = input("Entrez la priorité (Basse/Moyenne/Haute) : ")
        creer_ticket(description, priorite)
    elif choix == "2":
        afficher_tickets()
    elif choix == "3":
        try:
            ticket_id = int(input("Entrez l'ID du ticket à mettre à jour : "))
            nouveau_statut = input("Entrez le nouveau statut (Ouvert/Fermé) : ")
            mettre_a_jour_statut(ticket_id, nouveau_statut)
        except ValueError:
            print("Veuillez entrer un ID valide.")
    elif choix == "4":
        try:
            ticket_id = int(input("Entrez l'ID du ticket à supprimer : "))
            supprimer_ticket(ticket_id)
        except ValueError:
            print("Veuillez entrer un ID valide.")
    elif choix == "5":
        sauvegarder_tickets('tickets.json')
    elif choix == "6":
        print("Au revoir !")
        sauvegarder_tickets('tickets.json')  # Sauvegarde automatique avant de quitter
        break
    elif choix == "7":
        critere = input("Entrez un mot-clé ou une partie de la description à rechercher : ")
        rechercher_ticket(critere)
    elif choix == "8":
        fichier = input("Entrez le nom du fichier d'export (ex: tickets.txt) : ")
        exporter_tickets(fichier)
    else:
        print("Choix invalide. Veuillez réessayer.")
