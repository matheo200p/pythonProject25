from dataclasses import dataclass
import pygame,pytmx, pyscroll


@dataclass


class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup

    class MapManager:
        def __init__(self, screen, player):
            self.scree = screen
            self.player = player
            self.maps = dict()_# "house" -> map("house", walls, group)
            self.current_map = "world"

            def register_map(self, name):
                # Charger la carte clasique
                tmx_data = pytmx.util_pygame.load_pygame ( f"../map/{name}.tmx" )
                map_data = pyscroll.data.TiledMapData ( tmx_data )
                map_layer = pyscroll.orthographic.BufferedRenderer ( map_data, self.screen.get_size () )
                map_layer.zoom = 2

                # Les collisions
                walls = []

                for obj in tmx_data.objects:
                    if obj.type == "collision":
                        walls.append ( pygame.Rect ( obj.x, obj.y, obj.width, obj.height ) )

                # Dessiner les différents calques
                group = pyscroll.PyscrollGroup ( map_layer=map_layer, default_layer=5 )
                group.add ( self.player )

              # creer un objet map
                self.maps[name] = map(name, walls, group)

