import sys
from typing import Dict

class Mesto:
    def __init__(self) -> None:
        self.sousedi: Dict[str, int] = {}

    def pridat_souseda(self, soused: str, vzdalenost: int) -> None:
        self.sousedi[soused] = vzdalenost

class Graph:
    def __init__(self) -> None:
        self.mesta: Dict[str, Mesto] = {}

    def vrat_nebo_zaloz(self, nazev: str) -> Mesto:
        if nazev not in self.mesta:
            self.mesta[nazev] = Mesto()
        return self.mesta[nazev]

    def new_edge(self, z_mesta: str, do_mesta: str, vzdalenost: int) -> None:
        mesto1 = self.vrat_nebo_zaloz(z_mesta)
        mesto2 = self.vrat_nebo_zaloz(do_mesta)
        mesto1.pridat_souseda(do_mesta, vzdalenost)
        mesto2.pridat_souseda(z_mesta, vzdalenost)

    def find_shortest_path(self, from_city: str, to_city: str) -> int:
        if from_city not in self.mesta or to_city not in self.mesta:
            return sys.maxsize

        vzdalenosti: Dict[str, int] = {mesto: sys.maxsize for mesto in self.mesta}
        vzdalenosti[from_city] = 0
        navstivena = set()

        while True:
            # vyber nenavštívené město s nejmenší vzdáleností
            aktualni_mesto = None
            max_vzdalenost = sys.maxsize
            for mesto, vzdalenost in vzdalenosti.items():
                if mesto not in navstivena and vzdalenost < max_vzdalenost:
                    aktualni_mesto = mesto
                    max_vzdalenost = vzdalenost

            if aktualni_mesto is None:
                break  # Všechna dosažitelná města byla navštívena

            if aktualni_mesto == to_city:
                return vzdalenosti[to_city]

            navstivena.add(aktualni_mesto)

            for soused, vzdalenost in self.mesta[aktualni_mesto].sousedi.items():
                if soused in navstivena:
                    continue
                nova_vzdalenost = vzdalenosti[aktualni_mesto] + vzdalenost
                if nova_vzdalenost < vzdalenosti[soused]:
                    vzdalenosti[soused] = nova_vzdalenost

        return vzdalenosti[to_city]

