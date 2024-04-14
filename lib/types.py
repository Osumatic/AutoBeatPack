"""
Beatmap types and naming conventions
"""

pack_types = {
    "standard": {
        "example": "{prefix}{suffix}{num} - {mode} Beatmap Pack #{num}",
        "prefix": "S",
        "subtypes": {
            "osu!": {
                "suffix": "",
                "mode": "osu!"
            },
            "osu!taiko": {
                "suffix": "T",
                "mode": "osu!taiko"
            },
            "osu!mania": {
                "suffix": "M",
                "mode": "osu!mania"
            },
            "osu!catch": {
                "suffix": "C",
                "mode": "osu!catch"
            }
        }
    },
    "featured artist": {
        "example": "{prefix}{num} - {artistname} Pack",
        "prefix": "F"
    },
    "tournament": {
        "example": "{prefix}{num} - {tournamentname}: {stage} Pack",
        "prefix": "P"
    },
    "loved": {
        "example": "{prefix}{num} - Project Loved: {season} ({mode})",
        "prefix": "L"
    },
    "spotlights": {
        "example": "{prefix}{num} - Beatmap Spotlights {season} ({mode})",
        "prefix": "R"
    },
    "theme": {
        "example": "{prefix}{suffix}{num} - {packname}",
        "prefix": "T",
        "subtypes": {
            "centurion": {
                "example": "{prefix}{suffix}{num} - Centurion Pack: {mapper}",
                "suffix": "M"
            }
        }
    },
    "artist/album": {
        "example": "{prefix}{num} - {packname}",
        "prefix": "A"
    }
}
