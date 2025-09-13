"""Game scenes implementing the full quest storyline.

Scene order:
1. Walk to the highlighted grandfather.
2. Talk with grandfather.
3. Walk to the highlighted grandmother.
4. Talk with grandmother (asks for a flower).
5. Walk to the highlighted flower.
6. Talk with flower (learn the word).
7. Return to highlighted grandmother.
8. Final dialog with grandmother.

Interacting with a highlighted object adds the corresponding word and
placeholder image to the player's inventory.
"""

from scene import Scene, StaticObject, NPC, Rect


def scene1() -> Scene:
    """Walking scene with highlighted grandfather."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        name="Бабай",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=True,
        next_scene_factory=scene2,
        texture_path="sprites/objects/grandpa_highlited.png",
        z=2,
    )
    ebi = StaticObject(
        id="ebi",
        name="Әби",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandma.png",
        z=2,
    )
    flower = StaticObject(
        id="flower",
        name="Чәчәк",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=2,
    )
    return Scene(
        id="scene1",
        objects=[background, house1, house2, babay, ebi, flower],
        player_pos=(230, 220),
        player_size=(16, 16),
        interact_distance=28.0,
        player_texture_path="sprites/bahtiyar/down0.png",
        scale_player_texture_to_rect=True,
        player_z=3,
    )


def scene2() -> Scene:
    """Dialog with grandfather teaching the word 'бабай'."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    ebi = StaticObject(
        id="ebi",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandma.png",
        z=1,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=1,
    )
    babay_big = NPC(
        id="babay_big",
        name="Бабай",
        rect=Rect(20, 20, 220, 259),
        solid=False,
        interactable=True,
        dialog_lines=["Сәлам!"],
        repeatable=False,
        persist_progress=True,
        texture_path="sprites/objects/grandpa.png",
        z=2,
        reward=("бабай", "sprites/objects/grandpa.png"),
        next_scene_factory=scene3,
    )
    scene = Scene(
        id="scene2",
        objects=[background, house1, house2, ebi, flower, babay_big],
        player_pos=(-100, -100),
        player_size=(16, 16),
        player_texture_path="sprites/bahtiyar/down0.png",
        player_z=-1,
    )
    scene.start_dialog_with(babay_big)
    return scene


def scene3() -> Scene:
    """Walking scene with highlighted grandmother."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=2,
    )
    ebi = StaticObject(
        id="ebi",
        name="Әби",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=True,
        next_scene_factory=scene4,
        texture_path="sprites/objects/grandma_highlited.png",
        z=2,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=2,
    )
    return Scene(
        id="scene3",
        objects=[background, house1, house2, babay, ebi, flower],
        player_pos=(230, 220),
        player_size=(16, 16),
        interact_distance=28.0,
        player_texture_path="sprites/bahtiyar/down0.png",
        scale_player_texture_to_rect=True,
        player_z=3,
    )


def scene4() -> Scene:
    """Dialog with grandmother asking for a flower."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=1,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=1,
    )
    ebi_big = NPC(
        id="ebi_big",
        name="Әби",
        rect=Rect(20, 20, 220, 259),
        solid=False,
        interactable=True,
        dialog_lines=["Исәнмесез, бир миңа чәчәк"],
        repeatable=False,
        persist_progress=True,
        texture_path="sprites/objects/grandma.png",
        z=2,
        reward=("әби", "sprites/objects/grandma.png"),
        next_scene_factory=scene5,
    )
    scene = Scene(
        id="scene4",
        objects=[background, house1, house2, babay, flower, ebi_big],
        player_pos=(-100, -100),
        player_size=(16, 16),
        player_texture_path="sprites/bahtiyar/down0.png",
        player_z=-1,
    )
    scene.start_dialog_with(ebi_big)
    return scene


def scene5() -> Scene:
    """Walking scene with highlighted flower."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=2,
    )
    ebi = StaticObject(
        id="ebi",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandma.png",
        z=2,
    )
    flower = StaticObject(
        id="flower",
        name="Чәчәк",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=True,
        next_scene_factory=scene6,
        texture_path="sprites/objects/flower_highlited.png",
        z=2,
    )
    return Scene(
        id="scene5",
        objects=[background, house1, house2, babay, ebi, flower],
        player_pos=(230, 220),
        player_size=(16, 16),
        interact_distance=28.0,
        player_texture_path="sprites/bahtiyar/down0.png",
        scale_player_texture_to_rect=True,
        player_z=3,
    )


def scene6() -> Scene:
    """Dialog with flower teaching the word 'чәчәк'."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=1,
    )
    ebi = StaticObject(
        id="ebi",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandma.png",
        z=1,
    )
    flower_big = NPC(
        id="flower_big",
        name="Чәчәк",
        rect=Rect(150, 30, 346, 250),
        solid=False,
        interactable=True,
        dialog_lines=["Чәчәк"],
        repeatable=False,
        persist_progress=True,
        texture_path="sprites/objects/flower.png",
        z=2,
        reward=("чәчәк", "sprites/objects/flower.png"),
        next_scene_factory=scene7,
    )
    scene = Scene(
        id="scene6",
        objects=[background, house1, house2, babay, ebi, flower_big],
        player_pos=(-100, -100),
        player_size=(16, 16),
        player_texture_path="sprites/bahtiyar/down0.png",
        player_z=-1,
    )
    scene.start_dialog_with(flower_big)
    return scene


def scene7() -> Scene:
    """Walking scene returning to grandmother with the flower."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=2,
    )
    ebi = StaticObject(
        id="ebi",
        name="Әби",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=True,
        next_scene_factory=scene8,
        texture_path="sprites/objects/grandma_highlited.png",
        z=2,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=2,
    )
    return Scene(
        id="scene7",
        objects=[background, house1, house2, babay, ebi, flower],
        player_pos=(230, 220),
        player_size=(16, 16),
        interact_distance=28.0,
        player_texture_path="sprites/bahtiyar/down0.png",
        scale_player_texture_to_rect=True,
        player_z=3,
    )


def scene8() -> Scene:
    """Final dialog where grandmother thanks the player."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=1,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=1,
    )
    ebi_big = NPC(
        id="ebi_big_final",
        name="Әби",
        rect=Rect(20, 20, 220, 259),
        solid=False,
        interactable=True,
        dialog_lines=["Рәхмәт"],
        repeatable=False,
        persist_progress=True,
        texture_path="sprites/objects/grandma.png",
        z=2,
        next_scene_factory=scene9,
    )
    scene = Scene(
        id="scene8",
        objects=[background, house1, house2, babay, flower, ebi_big],
        player_pos=(-100, -100),
        player_size=(16, 16),
        player_texture_path="sprites/bahtiyar/down0.png",
        player_z=-1,
    )
    scene.start_dialog_with(ebi_big)
    return scene


def scene9() -> Scene:
    """Final walking scene after grandmother thanks the player."""
    background = StaticObject(
        id="bg",
        rect=Rect(0, 0, 496, 279),
        solid=False,
        interactable=False,
        texture_path="sprites/backgrounds/root.png",
        z=0,
        scale_texture_to_rect=True,
    )
    house1 = StaticObject(
        id="house1",
        rect=Rect(40, 120, 120, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house1.png",
        z=1,
    )
    house2 = StaticObject(
        id="house2",
        rect=Rect(336, 120, 416, 200),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/house2.png",
        z=1,
    )
    babay = StaticObject(
        id="babay",
        rect=Rect(360, 150, 420, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandpa.png",
        z=2,
    )
    ebi = StaticObject(
        id="ebi",
        rect=Rect(80, 150, 140, 260),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/grandma.png",
        z=2,
    )
    flower = StaticObject(
        id="flower",
        rect=Rect(236, 210, 260, 238),
        solid=False,
        interactable=False,
        texture_path="sprites/objects/flower.png",
        z=2,
    )
    return Scene(
        id="scene9",
        objects=[background, house1, house2, babay, ebi, flower],
        player_pos=(230, 220),
        player_size=(16, 16),
        interact_distance=28.0,
        player_texture_path="sprites/bahtiyar/down0.png",
        scale_player_texture_to_rect=True,
        player_z=3,
    )


scenes = {
    "scene1": scene1(),
    "scene2": scene2(),
    "scene3": scene3(),
    "scene4": scene4(),
    "scene5": scene5(),
    "scene6": scene6(),
    "scene7": scene7(),
    "scene8": scene8(),
    "scene9": scene9(),
}

