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
                    range(1300, 1317+1): {
                        "mode": "",
                        "ext": "zip"
                    },
                    range(1318, 9999): {
                        "mode": "osu! ",
                        "ext": "zip"
                    }
                }
            },
            "osu!taiko": {
                "suffix": "T",
                "ranges": {
                    range(1, 224+1): {
                        "mode": "Taiko ",
                        "ext": "7z"
                    },
                    range(225, 236+1): {
                        "mode": "Taiko ",
                        "ext": "zip"
                    },
                    range(237, 9999): {
                        "mode": "osu!taiko ",
                        "ext": "zip"
                    }
                }
            },
            "osu!mania": {
                "suffix": "M",
                "ranges": {
                    range(1, 154+1): {
                        "mode": "Mania ",
                        "ext": "7z"
                    },
                    range(155, 172+1): {
                        "mode": "Mania ",
                        "ext": "zip"
                    },
                    range(173, 9999): {
                        "mode": "osu!mania ",
                        "ext": "zip"
                    }
                }
            },
            "osu!catch": {
                "suffix": "C",
                "ranges": {
                    range(1, 57+1): {
                        "mode": "Catch the Beat ",
                        "ext": "7z"
                    },
                    range(58, 58+1): {
                        "mode": "osu!catch ",
                        "ext": "zip"
                    },
                    range(59, 80+1): {
                        "mode": "Catch the Beat ",
                        "ext": "7z"
                    },
                    range(81, 85+1): {
                        "mode": "Catch the Beat ",
                        "ext": "zip"
                    },
                    range(86, 9999): {
                        "mode": "osu!catch ",
                        "ext": "zip"
                    }
                }
            }
        }
    },
    "featured artist": {
        "template": "{prefix}{num} - {artist} Pack.zip",
        "prefix": "F",
        "artists": ["USAO", "Rohi", "in love with a ghost"]
    },
    "tournament": {
        "template": "{prefix}{num} - {mode} World Cup {year}: {stage} Pack",
        "prefix": "P",
        "years": range(2015, 2024+1),
        "stages": ["Group Stage", "Round of {count}", "Quarterfinals", "Semifinals", "Finals"],
        "subtypes": {
            "osu!": {},
            "osu!taiko": {},
            "osu!mania 4K": {},
            "osu!mania 7K": {},
            "osu!catch": {}
        }
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
