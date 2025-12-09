import json
from pathlib import Path
from db.models import Race, Skill, Guild, Player


def main() -> None:
    players_file = Path(__file__).resolve().parent / "players.json"

    with open(players_file, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    # normalize to a list of player entries (accept dict or string entries)
    if isinstance(players_data, dict):
        # some fixtures may wrap the list under a top-level key
        players_data = players_data.get("players", [])
    if not isinstance(players_data, list):
        players_data = [players_data]

    for raw_player in players_data:
        # allow a player to be a dict or a simple string (nickname)
        if isinstance(raw_player, str):
            player = {"nickname": raw_player}
        elif isinstance(raw_player, dict):
            player = raw_player
        else:
            # unexpected type: skip
            continue

        nickname = player.get("nickname")
        if not nickname:
            continue

        race_data = player.get("race") or {}
        if isinstance(race_data, dict):
            race_name = race_data.get("name", "")
            race_description = race_data.get("description", "")
            skills_list = race_data.get("skills", [])
        elif isinstance(race_data, str):
            race_name = race_data
            race_description = ""
            skills_list = []
        else:
            race_name = ""
            race_description = ""
            skills_list = []

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in skills_list:
            if isinstance(skill_data, dict):
                skill_name = skill_data.get("name")
                bonus = skill_data.get("bonus", "")
            else:
                skill_name = skill_data
                bonus = ""

            if not skill_name:
                continue

            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": bonus,
                    "race": race,
                }
            )

        guild_data = player.get("guild")
        guild = None
        if isinstance(guild_data, dict):
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
        elif isinstance(guild_data, str):
            guild_name = guild_data
            guild_description = None
        else:
            guild_name = None
            guild_description = None

        if guild_name:
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
