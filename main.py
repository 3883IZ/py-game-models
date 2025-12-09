import json
from pathlib import Path
from db.models import Race, Skill, Guild, Player


def main():
    players_file = Path(__file__).resolve().parent / "players.json"

    with open(players_file, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for player in players_data:
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")}
        )

        for skill_data in player["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )

        guild = None
        if "guild" in player and player["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"].get("description")}
            )

        Player.objects.get_or_create(
            nickname=player["nickname"],
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
