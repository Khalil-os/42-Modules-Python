def main() -> None:
    print("=== Game Analytics Dashboard ===")

    players = [
        {"name": "alice", "score": 2300, "achievements": 5,
         "region": "north", "active": True},
        {"name": "bob", "score": 1800, "achievements": 3,
         "region": "east", "active": True},
        {"name": "charlie", "score": 2150, "achievements": 7,
         "region": "central", "active": True},
        {"name": "diana", "score": 2050, "achievements": 4,
         "region": "east", "active": False},
    ]

    achievements = [
        ("alice", "first_kill"),
        ("alice", "level_10"),
        ("alice", "boss_slayer"),
        ("alice", "treasure_hunter"),
        ("alice", "speed_runner"),
        ("bob", "first_kill"),
        ("bob", "level_10"),
        ("bob", "dungeon_master"),
        ("charlie", "first_kill"),
        ("charlie", "level_10"),
        ("charlie", "boss_slayer"),
        ("charlie", "dragon_slayer"),
    ]

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print("High scorers (>2000):", high_scorers)

    doubled_scores = [p["score"] * 2 for p in players]
    print("Scores doubled:", doubled_scores)

    active_players = [p["name"] for p in players if p["active"]]
    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players if p["active"]}
    print("Player scores:", player_scores)

    score_categories = {
        "high": sum(1 for p in players if p["score"] > 2000),
        "medium": sum(1 for p in players if 1000 <= p["score"] <= 2000),
        "low": sum(1 for p in players if p["score"] < 1000),
    }
    print("Score categories:", score_categories)

    achievement_counts = {p["name"]: p["achievements"]
                          for p in players if p["active"]}
    print("Achievement counts:", achievement_counts)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)

    unique_achievements = {a[1] for a in achievements}
    print("Unique achievements:", unique_achievements)

    active_regions = {p["region"] for p in players if p["active"]}
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    print("Total players:", len(players))
    print("Total unique achievements:", len(achievements))

    avg_score = sum(p["score"] for p in players) / len(players)
    print("Average score:", avg_score)

    top_player = max(players, key=lambda p: p["score"])
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, "
        f"{top_player['achievements']} achievements)"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
