# Classe TDS (Table des Symboles)
class TDS:
    def __init__(self, region_id, pere):
        """
        Initialisation de la structure TDS (Table des Symboles).
        Chaque région correspond à une portée dans le code source.

        Args:
        - region_id (int): Identifiant unique pour chaque région.
        - pere (int): Référence à la région parent. None si la région est la racine.

        Attributs:
        - fils (list): Liste des régions enfant de cette région.
        - frere (int): Identifiant du frère immédiat dans l'arbre des régions (si présent).
        - declaration (list): Liste des identifiants déclarés dans cette région.
        """
        self.region_id = region_id
        self.pere = pere
        self.fils = []
        self.frere = None
        self.declaration = []

# Fonction de création de la table des symboles (TDS)
def creation_TDS(Tokens):
    """
    Génère la structure de la table des symboles (TDS) à partir des tokens fournis.

    Args:
    - Tokens (list): Liste de tokens, chacun représentant un élément lexical du code source.

    Returns:
    - dict: Dictionnaire où chaque clé est un identifiant de région (int)
      et chaque valeur est une instance de la classe TDS.
    """
    derniere_region_traite = 0  # Identifiant de la dernière région traitée
    regions = {}  # Dictionnaire pour stocker les régions
    regions[0] = TDS(0, None)  # Initialisation de la racine (région 0)
    pile_regions = [0]  # Pile pour suivre les régions imbriquées

    for token in Tokens:
        if token.type.value == "INDENT":
            # Création d'une nouvelle région pour un bloc indenté
            derniere_region_traite += 1
            regions[derniere_region_traite] = TDS(derniere_region_traite, pile_regions[-1])
            
            # Si la région parente a des fils, définir le frère de son dernier fils
            if len(regions[pile_regions[-1]].fils) > 0:
                prev_fils = regions[pile_regions[-1]].fils[-1]
                regions[prev_fils].frere = derniere_region_traite
            
            # Ajouter cette région comme un fils de la région parente
            regions[pile_regions[-1]].fils.append(derniere_region_traite)
            
            # Ajouter la nouvelle région à la pile
            pile_regions.append(derniere_region_traite)
            
        elif token.type.value == "DEDENT":
            # Sortie d'une région (fin du bloc indenté)
            pile_regions.pop()
        
        elif token.type.value == "IDENTIFIER":
            # Enregistrer un identifiant déclaré dans la région actuelle
            regions[pile_regions[-1]].declaration.append(token)
    
    return regions

# Fonction de représentation de la TDS
def representation_TDS(tds):
    """
    Affiche une représentation textuelle de la structure de la table des symboles (TDS).

    Args:
    - tds (dict): Dictionnaire contenant les régions et leurs informations.
    """
    for region_id, region in tds.items():
        print(f"Région {region_id}:")
        print(f"  Père : {region.pere if region.pere is not None else 'Aucun'}")
        print(f"  Fils : {region.fils if region.fils else 'Aucun'}")
        print(f"  Frère : {region.frere if region.frere is not None else 'Aucun'}")
        print(f"  Déclarations : {region.declaration if region.declaration else 'Aucune'}")
        print("-" * 40)
