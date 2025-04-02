class Mesto:
    def __init__(self, nazev: str) -> None:
        self.nazev = nazev
        self.sousedi: dict[Mesto, int] = {}

    def pridat_souseda(self, soused: "Mesto", vzdalenost: int) -> None:
        self.sousedi[soused] = vzdalenost

class Graph:
    def __init__(self) -> None:
        self.mesta: dict[str, Mesto] = {}

    def vrat_nebo_zaloz(self, nazev: str) -> Mesto:
        if nazev not in self.mesta:
            self.mesta[nazev] = Mesto(nazev)
        return self.mesta[nazev]

    def new_edge(self, z_mesta: str, do_mesta: str, vzdalenost: int) -> None:
        mesto1 = self.vrat_nebo_zaloz(z_mesta)
        mesto2 = self.vrat_nebo_zaloz(do_mesta)
        mesto1.pridat_souseda(mesto2, vzdalenost)
        mesto2.pridat_souseda(mesto1, vzdalenost)  

    def find_shortest_path(self, from_city: str, to_city: str) -> int:
        if from_city not in self.mesta or to_city not in self.mesta:
            return float('inf')
        
        start = self.mesta[from_city]
        cil = self.mesta[to_city]
        
        vzdalenosti = {mesto: float('inf') for mesto in self.mesta.values()}
        vzdalenosti[start] = 0
        
        aktualni_mesto = start  
        
        prosla_mesta: dict[Mesto, int] = {}                  
        
        
        while True:
            
            prosla_mesta[aktualni_mesto] = 0           
            
            if aktualni_mesto == cil:
                return vzdalenosti[cil]

            nejblizsi_vzdalenost = float('inf')

            for soused, vzdalenost in aktualni_mesto.sousedi.items():
                nova_vzdalenost = vzdalenosti[aktualni_mesto] + vzdalenost
                
                if  soused in prosla_mesta:
                    continue

                if nova_vzdalenost < vzdalenosti[soused]:
                    vzdalenosti[soused] = nova_vzdalenost
                
                if nova_vzdalenost < nejblizsi_vzdalenost:
                    nejblizsi_vzdalenost = nova_vzdalenost
                    nejblizsi_soused = soused
            
            start = aktualni_mesto
            aktualni_mesto = nejblizsi_soused
                                
        
        return float('inf')  # Pokud neexistuje cesta
