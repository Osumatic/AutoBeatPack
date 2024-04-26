"""
Beatmap types and naming conventions
"""

PACK_TYPES = {
    "standard": {
        "title": "Standard",
        "prefix": "S",
        "subtypes": {
            "osu!": {
                "title": "osu!",
                "prefix": ""
            },
            "osu!taiko": {
                "title": "osu!taiko",
                "prefix": "T"
            },
            "osu!mania": {
                "title": "osu!mania",
                "prefix": "M"
            },
            "osu!catch": {
                "title": "osu!catch",
                "prefix": "C"
            }
        }
    },
    "featured": {
        "title": "Featured Artist",
        "prefix": "F"
    },
    "tournament": {
        "title": "Tournament",
        "prefix": "P",
    },
    "loved": {
        "title": "Loved",
        "prefix": "L"
    },
    "chart": {
        "title": "Spotlights",
        "prefix": "R"
    },
    "theme": {
        "title": "Theme",
        "prefix": "T",
    },
    "artist": {
        "title": "Artist-Album",
        "prefix": "A"
    }
}
