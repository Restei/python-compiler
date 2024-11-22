class TDS:
    def __init__(self, region_id,pere):
        self.region_id = region_id
        self.pere = pere
        self.fils = []
        self.frere = -1
        self.declaration = []

def creation_TDS(Tokens):
    derniere_region_traite = 0
    regions = {}
    regions[0] = TDS(0,-1)
    pile_regions = [0]
    
    for token in Tokens:
        if  token.type.value == "INDENT":
            derniere_region_traite += 1
            regions[derniere_region_traite] = TDS(derniere_region_traite, pile_regions[-1])
            
            if len(regions[pile_regions[-1]].fils) > 0:
                prev_fils = regions[pile_regions[-1]].fils[-1]
                regions[prev_fils].frere = derniere_region_traite
            
            regions[pile_regions[-1]].fils.append(derniere_region_traite)

            
            pile_regions.append(derniere_region_traite)
            
        elif token.type.value == "DEDENT":
            pile_regions.pop()
        
        elif token.type.value == "IDENTIFIER":
            regions[pile_regions[-1]].declaration.append(token)
    return regions
