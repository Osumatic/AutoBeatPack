"""
Beatmap types and naming conventions
"""

pack_types = {
    "standard": {
        "template": "{prefix}{suffix}{num} - {mode}Beatmap Pack #{num}.{ext}",
        "prefix": "S",
        "subtypes": {
            "osu!": {
                "suffix": "",
                "ranges": {
                    range(1, 1299+1): {
                        "mode": "",
                        "ext": "7z"
                    },
                    range(1299+1, 1317+1): {
                        "mode": "",
                        "ext": "zip"
                    },
                    range(1371+1, 9999): {
                        "mode": "osu! ",
                        "ext": "zip"
                    }
                }
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
        "template": "{prefix}{num} - {artistname} Pack",
        "prefix": "F"
    },
    "tournament": {
        "template": "{prefix}{num} - {tournamentname}: {stage} Pack",
        "prefix": "P"
    },
    "loved": {
        "template": "{prefix}{num} - Project Loved: {season} ({mode})",
        "prefix": "L"
    },
    "spotlights": {
        "template": "{prefix}{num} - Beatmap Spotlights {season} ({mode})",
        "prefix": "R"
    },
    "theme": {
        "template": "{prefix}{suffix}{num} - {packname}",
        "prefix": "T",
        "subtypes": {
            "centurion": {
                "template": "{prefix}{suffix}{num} - Centurion Pack: {mapper}",
                "suffix": "M"
            }
        }
    },
    "artist/album": {
        "template": "{prefix}{num} - {packname}",
        "prefix": "A"
    }
}
