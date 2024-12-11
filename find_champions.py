def find_champions(players):
    """
    Trouve les champions parmi une liste de joueurs d'échecs.
    Un joueur est champion si personne ne peut l'éliminer, c'est-à-dire :
    - Personne n'est strictement plus jeune et plus fort (même score inclus).
    - Personne n'est strictement plus fort et du même âge ou plus jeune.
    
    Args:
        players (list): Une liste de tuples (nom, âge, score).
        
    Returns:
        list: Une liste de joueurs champions.
    """
    if not players:  # Cas particulier : liste vide
        return []

    # Tri des joueurs : par âge croissant, puis score décroissant
    players.sort(key=lambda x: (x[1], -x[2]))

    champions = []
    max_score_seen = -1  # Score maximum vu pour les joueurs précédents
    current_age_group = None  # Suivi de l'âge pour inclure les joueurs de même âge/score

    # Parcours des joueurs triés
    for player in players:
        name, age, score = player

        # Vérifie si le joueur est un champion
        if (score > max_score_seen) or ((score == max_score_seen) and (age == current_age_group)):
            champions.append(player)  # Ajoute le joueur aux champions
            max_score_seen = score  # Met à jour le score maximum vu

        # Met à jour l'âge courant
        current_age_group = age

    return champions


# Exemple d'utilisation
players = [
    ("Alice", 30, 2400),
    ("Bob", 28, 2500),
    ("Charlie", 32, 2300),
    ("Diana", 28, 2500),  # Cas particulier : même âge et score qu'Alice
]

champions = find_champions(players)
if not champions:
    print("Pas de champions trouvés.")
else:
    print("Les champions sont :", champions)

