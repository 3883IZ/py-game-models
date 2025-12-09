from db.models import Race, Skill, Guild, Player


def main() -> None:
    Player.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Race.objects.all().delete()

    elf = Race.objects.create(
        name="elf",
        description="The magic race",
    )
    human = Race.objects.create(
        name="human",
        description="Human race",
    )

    Skill.objects.create(
        name="Teleportation",
        bonus=(
            "The ability to move so fast they look like they're "
            "teleporting. Could be considered to technically be "
            "Teleportation."
        ),
        race=elf,
    )
    Skill.objects.create(
        name="Reality Warping",
        bonus=(
            "The ability to Warp Reality. Make the impossible become "
            "possible but can't warp anything containing the structure "
            "that holds everything together (Which are many creatures.)"
        ),
        race=elf,
    )

    archers = Guild.objects.create(
        name="archers",
    )
    mags = Guild.objects.create(
        name="mags",
        description="A community of the elf mags",
    )
    blacksmiths = Guild.objects.create(
        name="blacksmiths",
        description="A community of the blacksmiths",
    )

    Player.objects.create(
        nickname="john",
        email="john@gmail.com",
        bio="Hello, I'm John, elf ranger",
        race=elf,
        guild=archers,
    )
    Player.objects.create(
        nickname="max",
        email="max@gmail.com",
        bio="Hello, I'm Max, elf mag",
        race=elf,
        guild=mags,
    )
    Player.objects.create(
        nickname="arthur",
        email="arthur@gmail.com",
        bio="Arthur, elf mag",
        race=elf,
        guild=mags,
    )
    Player.objects.create(
        nickname="andrew",
        email="andrew@gmail.com",
        bio="Hello, I'm Andrew",
        race=human,
        guild=blacksmiths,
    )
    Player.objects.create(
        nickname="nick",
        email="nick@gmail.com",
        bio="Hello, I'm Nick",
        race=human,
        guild=None,
    )


if __name__ == "__main__":
    main()
