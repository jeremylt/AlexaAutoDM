"""
This code provides an Auto DM for tabletop RPG games that provides monsters
within given specifications (Challange Rating and Environment).
"""

from __future__ import print_function
import random

# --------------------------- Dictionary of monsters ---------------------------

allmonsters = [{"Name" : "commoner",
                "CR"   : "0",
                "Env"  : ["arctic", "coastal", "desert", "forest", "grassland", "hill", "urban"]},
               {"Name" : "Owl",
                "CR"   : "0",
                "Env"  : ["arctic", "forest"]},
               {"Name" : "bandit",
                "CR"   : "1/8",
                "Env"  : ["artic", "costal", "desert", "forest", "hill", "urban"]},
               {"Name" : "blood hawk",
                "CR"   : "1/8",
                "Env"  : ["arctic", "coastal", "forest", "grassland", "hill", "mountain"]},
               {"Name" : "kobold",
                "CR"   : "1/8",
                "Env"  : ["arctic", "coastal", "desert", "forest", "hill", "mountain", "swamp", "underdark", "urban"]},
               {"Name" : "tribal warrior",
                "CR"   : "1/8",
                "Env"  : ["arctic", "coastal", "desert", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "giant owl",
                "CR"   : "1/4",
                "Env"  : ["arctic"]},
               {"Name" : "winged kobold",
                "CR"   : "1/4",
                "Env"  : ["arctic", "coastal", "desert", "forest", "hill", "mountain", "swamp", "underdark", "urban"]},
               {"Name" : "ice mephit",
                "CR"   : "1/2",
                "Env"  : ["arctic"]},
               {"Name" : "orc",
                "CR"   : "1/2",
                "Env"  : ["arctic", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "scout",
                "CR"   : "1/2",
                "Env"  : ["arctic", "coastal", "desert", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "brown bear",
                "CR"   : "1",
                "Env"  : ["arctic", "forest", "hill"]},
               {"Name" : "half ogre",
                "CR"   : "1",
                "Env"  : ["arctic", "forest", "hill", "mountain", "underdark", "urban"]},
               {"Name" : "crab",
                "CR"   : "0",
                "Env"  : ["coastal"]},
               {"Name" : "eagle",
                "CR"   : "0",
                "Env"  : ["coastal", "grassland", "hill", "mountain"]},
               {"Name" : "giant crab",
                "CR"   : "1/8",
                "Env"  : ["coastal"]},
               {"Name" : "guard",
                "CR"   : "1/8",
                "Env"  : ["coastal", "desert", "forest", "grassland", "hill", "mountain", "urban"]},
               {"Name" : "merfolk",
                "CR"   : "1/8",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "poisonous snake",
                "CR"   : "1/8",
                "Env"  : ["coastal", "desert", "forest", "grassland", "hill", "swamp"]},
               {"Name" : "stirge",
                "CR"   : "1/8",
                "Env"  : ["coastal", "desert", "forest", "grassland", "hill", "mountain", "swamp", "underdark", "urban"]},
               {"Name" : "giant lizard",
                "CR"   : "1/4",
                "Env"  : ["coastal", "desert", "forest", "swamp", "underdark"]},
               {"Name" : "giant wolf spider",
                "CR"   : "1/4",
                "Env"  : ["coastal", "desert", "forest", "grassland", "hill"]},
               {"Name" : "pseudodragon",
                "CR"   : "1/4",
                "Env"  : ["coastal", "desert", "forest", "hill", "mountain", "urban"]},
               {"Name" : "pteranodon",
                "CR"   : "1/4",
                "Env"  : ["coastal", "grassland", "mountain"]},
               {"Name" : "sahuagin",
                "CR"   : "1/2",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "giant eagle",
                "CR"   : "1",
                "Env"  : ["coastal", "grassland", "hill", "mountain"]},
               {"Name" : "giant toad",
                "CR"   : "1",
                "Env"  : ["coastal", "desert", "forest", "swamp", "underdark"]},
               {"Name" : "harpy",
                "CR"   : "1",
                "Env"  : ["coastal", "forest", "hill", "mountain"]},
               {"Name" : "cat",
                "CR"   : "0",
                "Env"  : ["desert", "forest", "grassland", "urban"]},
               {"Name" : "hyena",
                "CR"   : "0",
                "Env"  : ["desert", "forest", "grassland", "hill"]},
               {"Name" : "jackal",
                "CR"   : "0",
                "Env"  : ["desert", "grassland"]},
               {"Name" : "scorpion",
                "CR"   : "0",
                "Env"  : ["desert"]},
               {"Name" : "vulture",
                "CR"   : "0",
                "Env"  : ["desert", "grassland", "hill"]},
               {"Name" : "camel",
                "CR"   : "1/8",
                "Env"  : ["desert"]},
               {"Name" : "flying snake",
                "CR"   : "1/8",
                "Env"  : ["desert", "forest", "grassland", "urban"]},
               {"Name" : "mule",
                "CR"   : "1/8",
                "Env"  : ["desert", "hill", "urban"]},
               {"Name" : "constrictor snake",
                "CR"   : "1/4",
                "Env"  : ["desert", "forest", "underwater"]},
               {"Name" : "giant poisonous snake",
                "CR"   : "1/4",
                "Env"  : ["desert", "forest", "grassland", "underdark", "urban"]},
               {"Name" : "dust mephit",
                "CR"   : "1/2",
                "Env"  : ["desert"]},
               {"Name" : "gnoll",
                "CR"   : "1/2",
                "Env"  : ["desert", "forest", "grassland", "hill"]},
               {"Name" : "hobgoblin",
                "CR"   : "1/2",
                "Env"  : ["desert", "forest", "grassland", "hill", "underdark"]},
               {"Name" : "jackalwere",
                "CR"   : "1/2",
                "Env"  : ["desert", "grassland"]},
               {"Name" : "swarm of insects",
                "CR"   : "1/2",
                "Env"  : ["desert", "forest", "grassland", "hill", "swamp", "underdark", "urban"]},
               {"Name" : "death dog",
                "CR"   : "1",
                "Env"  : ["desert"]},
               {"Name" : "giant hyena",
                "CR"   : "1",
                "Env"  : ["desert", "forest", "grassland", "hill"]},
               {"Name" : "giant spider",
                "CR"   : "1",
                "Env"  : ["desert", "forest", "underdark", "urban"]},
               {"Name" : "giant vulture",
                "CR"   : "1",
                "Env"  : ["desert", "grassland"]},
               {"Name" : "lion",
                "CR"   : "1",
                "Env"  : ["desert", "grassland", "hill", "mountain"]},
               {"Name" : "thri-keen",
                "CR"   : "1",
                "Env"  : ["desert", "grassland"]},
               {"Name" : "yuan-ti pureblood",
                "CR"   : "1",
                "Env"  : ["desert", "forest", "swamp", "urban"]},
               {"Name" : "awakened shrub",
                "CR"   : "0",
                "Env"  : ["forest"]},
               {"Name" : "baboon",
                "CR"   : "0",
                "Env"  : ["forest", "hill"]},
               {"Name" : "badger",
                "CR"   : "0",
                "Env"  : ["forest"]},
               {"Name" : "deer",
                "CR"   : "0",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "giant rat",
                "CR"   : "1/8",
                "Env"  : ["forest", "swamp", "underdark", "urban"]},
               {"Name" : "giant weasel",
                "CR"   : "1/8",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "mastiff",
                "CR"   : "1/8",
                "Env"  : ["forest", "hill", "urban"]},
               {"Name" : "twig blight",
                "CR"   : "1/8",
                "Env"  : ["forest"]},
               {"Name" : "blink dog",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "boar",
                "CR"   : "1/4",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "elk",
                "CR"   : "1/4",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "giant badger",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "giant frog",
                "CR"   : "1/4",
                "Env"  : ["forest", "swamp"]},
               {"Name" : "giant owl",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "goblin",
                "CR"   : "1/4",
                "Env"  : ["forest", "grassland", "hill", "underdark"]},
               {"Name" : "kenku",
                "CR"   : "1/4",
                "Env"  : ["forest", "urban"]},
               {"Name" : "needle blight",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "panther",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "pixie",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "sprite",
                "CR"   : "1/4",
                "Env"  : ["forest"]},
               {"Name" : "swarm of ravens",
                "CR"   : "1/4",
                "Env"  : ["forest", "hill", "swamp", "urban"]},
               {"Name" : "wolf",
                "CR"   : "1/4",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "ape",
                "CR"   : "1/2",
                "Env"  : ["forest"]},
               {"Name" : "black bear",
                "CR"   : "1/2",
                "Env"  : ["forest"]},
               {"Name" : "giant wasp",
                "CR"   : "1/2",
                "Env"  : ["forest", "grassland", "urban"]},
               {"Name" : "lizardfolk",
                "CR"   : "1/2",
                "Env"  : ["forest", "swamp"]},
               {"Name" : "satyr",
                "CR"   : "1/2",
                "Env"  : ["forest"]},
               {"Name" : "vine blight",
                "CR"   : "1/2",
                "Env"  : ["forest"]},
               {"Name" : "worg",
                "CR"   : "1/2",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "bugbear",
                "CR"   : "1",
                "Env"  : ["forest", "grassland", "underdark"]},
               {"Name" : "dire wolf",
                "CR"   : "1",
                "Env"  : ["forest", "hill"]},
               {"Name" : "dryad",
                "CR"   : "1",
                "Env"  : ["forest"]},
               {"Name" : "faerie dragon",
                "CR"   : "1",
                "Env"  : ["forest"]},
               {"Name" : "goblin boss",
                "CR"   : "1",
                "Env"  : ["forest", "grassland", "hill", "underdark"]},
               {"Name" : "harpy",
                "CR"   : "1",
                "Env"  : ["forest", "hill", "mountain"]},
               {"Name" : "tiger",
                "CR"   : "1",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "goat",
                "CR"   : "0",
                "Env"  : ["grassland", "hill", "mountain", "urban"]},
               {"Name" : "axe beak",
                "CR"   : "1/4",
                "Env"  : ["grassland", "hill"]},
               {"Name" : "rinding horse",
                "CR"   : "1/4",
                "Env"  : ["grassland", "urban"]},
               {"Name" : "cockatrice",
                "CR"   : "1/2",
                "Env"  : ["grassland"]},
               {"Name" : "giant goat",
                "CR"   : "1/2",
                "Env"  : ["grassland", "hill"]},
               {"Name" : "tippogriff",
                "CR"   : "1",
                "Env"  : ["grassland", "hill", "mountain"]},
               {"Name" : "scarecrow",
                "CR"   : "1",
                "Env"  : ["grassland"]},
               {"Name" : "raven",
                "CR"   : "0",
                "Env"  : ["hill", "swamp", "urban"]},
               {"Name" : "swarm of bats",
                "CR"   : "1/4",
                "Env"  : ["hill", "mountain", "underdark", "urban"]},
               {"Name" : "aarakocra",
                "CR"   : "1/4",
                "Env"  : ["mountain"]},
               {"Name" : "rat",
                "CR"   : "0",
                "Env"  : ["swamp", "urban"]},
               {"Name" : "bullywug",
                "CR"   : "1/8",
                "Env"  : ["swamp"]},
               {"Name" : "mud mephit",
                "CR"   : "1/8",
                "Env"  : ["swamp"]},
               {"Name" : "crocodile",
                "CR"   : "1/2",
                "Env"  : ["swamp", "urban"]},
               {"Name" : "ghoul",
                "CR"   : "1",
                "Env"  : ["swamp", "underdark", "urban"]},
               {"Name" : "giant fire beetle",
                "CR"   : "0",
                "Env"  : ["underdark"]},
               {"Name" : "shrieker",
                "CR"   : "0",
                "Env"  : ["underdark"]},
               {"Name" : "myconid sprout",
                "CR"   : "0",
                "Env"  : ["underdark"]},
               {"Name" : "flumph",
                "CR"   : "1/8",
                "Env"  : ["underdark"]},
               {"Name" : "drow",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "giant bat",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "giant centipede",
                "CR"   : "1/4",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "grimlock",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "kuo-toa",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "troglodyte",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "violet fungus",
                "CR"   : "1/4",
                "Env"  : ["underdark"]},
               {"Name" : "darkmantle",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "deep gnome",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "gas spore",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "gray ooze",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "magma mephit",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "myconid adult",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "piercer",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "rust monster",
                "CR"   : "1/2",
                "Env"  : ["underdark"]},
               {"Name" : "shadow",
                "CR"   : "1/2",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "duergar",
                "CR"   : "1",
                "Env"  : ["underdark"]},
               {"Name" : "fire snake",
                "CR"   : "1",
                "Env"  : ["underdark"]},
               {"Name" : "kuo-toa whip",
                "CR"   : "1",
                "Env"  : ["underdark"]},
               {"Name" : "quaggoth spore servant",
                "CR"   : "1",
                "Env"  : ["underdark"]},
               {"Name" : "specter",
                "CR"   : "1",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "quipper",
                "CR"   : "0",
                "Env"  : ["underwater"]},
               {"Name" : "steam mephit",
                "CR"   : "1/4",
                "Env"  : ["underwater"]},
               {"Name" : "giant sea horse",
                "CR"   : "1/2",
                "Env"  : ["underwater"]},
               {"Name" : "reef shark",
                "CR"   : "1/2",
                "Env"  : ["underwater"]},
               {"Name" : "giant octopus",
                "CR"   : "1",
                "Env"  : ["underwater"]},
               {"Name" : "swarm of quippers",
                "CR"   : "1",
                "Env"  : ["underwater"]},
               {"Name" : "cultist",
                "CR"   : "1/8",
                "Env"  : ["urban"]},
               {"Name" : "noble",
                "CR"   : "1/8",
                "Env"  : ["urban"]},
               {"Name" : "pony",
                "CR"   : "1/8",
                "Env"  : ["urban"]},
               {"Name" : "acolyte",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "draft horse",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "skeleton",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "smoke mephit",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "swarm of rats",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "zombie",
                "CR"   : "1/4",
                "Env"  : ["urban"]},
               {"Name" : "thug",
                "CR"   : "1/2",
                "Env"  : ["urban"]},
               {"Name" : "warhorse",
                "CR"   : "1/2",
                "Env"  : ["urban"]},
               {"Name" : "bandit captain",
                "CR"   : "2",
                "Env"  : ["arctic", "coastal", "desert", "forest", "hill", "urban"]},
               {"Name" : "berserker",
                "CR"   : "2",
                "Env"  : ["arctic", "coastal", "desert", "forest", "hill", "mountain"]},
               {"Name" : "druid",
                "CR"   : "2",
                "Env"  : ["arctic", "coastal", "desert", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "griffon",
                "CR"   : "2",
                "Env"  : ["arctic", "coastal", "grassland", "hill", "mountain"]},
               {"Name" : "ogre",
                "CR"   : "2",
                "Env"  : ["arctic", "coastal", "desert", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "orc Eye of Gruumsh",
                "CR"   : "2",
                "Env"  : ["arctic", "forest", "grassland", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "orog",
                "CR"   : "2",
                "Env"  : ["arctic", "forest", "grassland", "hill", "mountain", "underdark"]},
               {"Name" : "polar bear",
                "CR"   : "2",
                "Env"  : ["arctic", "underdark"]},
               {"Name" : "saber toothed tiger",
                "CR"   : "2",
                "Env"  : ["arctic", "mountain"]},
               {"Name" : "manticore",
                "CR"   : "3",
                "Env"  : ["arctic", "coastal", "hill", "mountain"]},
               {"Name" : "veteran",
                "CR"   : "3",
                "Env"  : ["arctic", "coastal", "forest", "grassland", "hill", "mountain", "underdark", "urban"]},
               {"Name" : "winter wolf",
                "CR"   : "3",
                "Env"  : ["arctic"]},
               {"Name" : "yeti",
                "CR"   : "3",
                "Env"  : ["arctic"]},
               {"Name" : "revenant",
                "CR"   : "5",
                "Env"  : ["arctic", "desert", "forest", "hill", "swamp", "urban"]},
               {"Name" : "merrow",
                "CR"   : "2",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "plesiosaurus",
                "CR"   : "2",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "sahuagin priestess",
                "CR"   : "2",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "sea hag",
                "CR"   : "2",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "banshee",
                "CR"   : "4",
                "Env"  : ["coastal", "forest"]},
               {"Name" : "sahuagin baron",
                "CR"   : "5",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "water elemental",
                "CR"   : "5",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "giant constrictor snake",
                "CR"   : "2",
                "Env"  : ["desert", "forest", "swamp", "underdark"]},
               {"Name" : "gnoll pack lord",
                "CR"   : "2",
                "Env"  : ["desert", "forest", "grassland", "hill"]},
               {"Name" : "giant scorpion",
                "CR"   : "3",
                "Env"  : ["desert"]},
               {"Name" : "hobgoblin captain",
                "CR"   : "3",
                "Env"  : ["desert", "forest", "grassland", "hill", "underdark"]},
               {"Name" : "mummy",
                "CR"   : "3",
                "Env"  : ["desert"]},
               {"Name" : "phase spider",
                "CR"   : "3",
                "Env"  : ["desert", "forest", "grassland", "hill", "underdark", "urban"]},
               {"Name" : "wight",
                "CR"   : "3",
                "Env"  : ["desert", "swamp", "underdark", "urban"]},
               {"Name" : "yuan-ti malison",
                "CR"   : "3",
                "Env"  : ["desert", "forest", "swamp"]},
               {"Name" : "couatl",
                "CR"   : "4",
                "Env"  : ["desert", "forest", "grassland", "urban"]},
               {"Name" : "gnoll fand of Yeenoghu",
                "CR"   : "4",
                "Env"  : ["desert", "forest", "grassland", "hill"]},
               {"Name" : "lamia",
                "CR"   : "4",
                "Env"  : ["desert"]},
               {"Name" : "weretiger",
                "CR"   : "4",
                "Env"  : ["desert", "forest", "grassland"]},
               {"Name" : "air elemental",
                "CR"   : "5",
                "Env"  : ["desert", "mountain"]},
               {"Name" : "fire elemental",
                "CR"   : "5",
                "Env"  : ["desert"]},
               {"Name" : "revenant",
                "CR"   : "5",
                "Env"  : ["desert", "hill", "swamp"]},
               {"Name" : "ankheg",
                "CR"   : "2",
                "Env"  : ["forest"]},
               {"Name" : "awakened tree",
                "CR"   : "2",
                "Env"  : ["forest"]},
               {"Name" : "centaur",
                "CR"   : "2",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "ettercap",
                "CR"   : "2",
                "Env"  : ["forest"]},
               {"Name" : "faerie dragon",
                "CR"   : "2",
                "Env"  : ["forest"]},
               {"Name" : "giant boar",
                "CR"   : "2",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "giant elk",
                "CR"   : "2",
                "Env"  : ["forest", "grassland", "hill", "mountain"]},
               {"Name" : "grick",
                "CR"   : "2",
                "Env"  : ["forest", "underdark"]},
               {"Name" : "lizardfolk shaman",
                "CR"   : "2",
                "Env"  : ["forest"]},
               {"Name" : "pegasus",
                "CR"   : "2",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "swarm of poisonous snakes",
                "CR"   : "2",
                "Env"  : ["forest", "swamp"]},
               {"Name" : "wererat",
                "CR"   : "2",
                "Env"  : ["forest", "urban"]},
               {"Name" : "will-o-wisp",
                "CR"   : "2",
                "Env"  : ["forest", "swamp", "urban"]},
               {"Name" : "displacer beast",
                "CR"   : "3",
                "Env"  : ["forest"]},
               {"Name" : "green hag",
                "CR"   : "3",
                "Env"  : ["forest", "hill", "swamp"]},
               {"Name" : "owlbear",
                "CR"   : "3",
                "Env"  : ["forest"]},
               {"Name" : "werewolf",
                "CR"   : "3",
                "Env"  : ["forest", "hill"]},
               {"Name" : "wereboar",
                "CR"   : "4",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "gorgon",
                "CR"   : "5",
                "Env"  : ["forest", "grassland", "hill"]},
               {"Name" : "shambling mound",
                "CR"   : "5",
                "Env"  : ["forest", "swamp"]},
               {"Name" : "troll",
                "CR"   : "5",
                "Env"  : ["forest", "hill", "mountain", "swamp", "underdark"]},
               {"Name" : "unicorn",
                "CR"   : "5",
                "Env"  : ["forest"]},
               {"Name" : "allosaurus",
                "CR"   : "2",
                "Env"  : ["grassland"]},
               {"Name" : "ankheg",
                "CR"   : "2",
                "Env"  : ["grassland"]},
               {"Name" : "rhinoceros",
                "CR"   : "2",
                "Env"  : ["grassland"]},
               {"Name" : "ankylosaurus",
                "CR"   : "3",
                "Env"  : ["grassland"]},
               {"Name" : "bulette",
                "CR"   : "5",
                "Env"  : ["grassland", "hill", "mountain"]},
               {"Name" : "triceratops",
                "CR"   : "5",
                "Env"  : ["grassland"]},
               {"Name" : "ettin",
                "CR"   : "4",
                "Env"  : ["hill", "mountain", "underdark"]},
               {"Name" : "hill giant",
                "CR"   : "5",
                "Env"  : ["hill"]},
               {"Name" : "basilisk",
                "CR"   : "3",
                "Env"  : ["mountain"]},
               {"Name" : "hell hound",
                "CR"   : "3",
                "Env"  : ["mountain", "underdark"]},
               {"Name" : "ghast",
                "CR"   : "2",
                "Env"  : ["swamp", "underdark"]},
               {"Name" : "giant crocodile",
                "CR"   : "5",
                "Env"  : ["swamp"]},
               {"Name" : "carrion crawler",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "gargoyle",
                "CR"   : "2",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "gelatinous cube",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "gibbering mouther",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "intellect devourer",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "mimic",
                "CR"   : "2",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "minotaur skeleton",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "nothic",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "ochre jelly",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "quaggoth",
                "CR"   : "2",
                "Env"  : ["underdark"]},
               {"Name" : "doppelganger",
                "CR"   : "3",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "grell",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "hook horror",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "kuo-toa monitor",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "minotaur",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "quaggoth thonot",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "spectator",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "water weird",
                "CR"   : "3",
                "Env"  : ["underdark"]},
               {"Name" : "black pudding",
                "CR"   : "4",
                "Env"  : ["underdark"]},
               {"Name" : "bone naga",
                "CR"   : "4",
                "Env"  : ["underdark"]},
               {"Name" : "chuul",
                "CR"   : "4",
                "Env"  : ["underdark"]},
               {"Name" : "flameskull",
                "CR"   : "4",
                "Env"  : ["underdark"]},
               {"Name" : "ghost",
                "CR"   : "4",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "beholder zombie",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "drow elite warrior",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "earth elemental",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "otyugh",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "roper",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "salamander",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "umber hulk",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "vampire spawn",
                "CR"   : "5",
                "Env"  : ["underdark", "urban"]},
               {"Name" : "wraith",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "xorn",
                "CR"   : "5",
                "Env"  : ["underdark"]},
               {"Name" : "hunter shark",
                "CR"   : "2",
                "Env"  : ["underwater"]},
               {"Name" : "killer whale",
                "CR"   : "3",
                "Env"  : ["underwater"]},
               {"Name" : "giant shark",
                "CR"   : "5",
                "Env"  : ["underwater"]},
               {"Name" : "cult fanatic",
                "CR"   : "2",
                "Env"  : ["urban"]},
               {"Name" : "priest",
                "CR"   : "2",
                "Env"  : ["urban"]},
               {"Name" : "knight",
                "CR"   : "3",
                "Env"  : ["urban"]},
               {"Name" : "succubus",
                "CR"   : "4",
                "Env"  : ["urban"]},
               {"Name" : "incubus",
                "CR"   : "4",
                "Env"  : ["urban"]},
               {"Name" : "cambion",
                "CR"   : "5",
                "Env"  : ["urban"]},
               {"Name" : "gladiator",
                "CR"   : "5",
                "Env"  : ["urban"]},
               {"Name" : "mammoth",
                "CR"   : "6",
                "Env"  : ["arctic"]},
               {"Name" : "young white dragon",
                "CR"   : "6",
                "Env"  : ["arctic"]},
               {"Name" : "frost giant",
                "CR"   : "8",
                "Env"  : ["arctic", "mountain"]},
               {"Name" : "abominable yeti",
                "CR"   : "9",
                "Env"  : ["arctic"]},
               {"Name" : "remorhaz",
                "CR"   : "11",
                "Env"  : ["arctic"]},
               {"Name" : "roc",
                "CR"   : "11",
                "Env"  : ["arctic", "coastal", "desert", "hill", "mountain"]},
               {"Name" : "adult white dragon",
                "CR"   : "13",
                "Env"  : ["arctic"]},
               {"Name" : "ancient white dragon",
                "CR"   : "20",
                "Env"  : ["arctic"]},
               {"Name" : "cyclops",
                "CR"   : "6",
                "Env"  : ["coastal", "desert", "grassland", "hill", "mountain", "underdark"]},
               {"Name" : "young bronze dragon",
                "CR"   : "8",
                "Env"  : ["coastal"]},
               {"Name" : "young blue dragon",
                "CR"   : "9",
                "Env"  : ["coastal", "desert"]},
               {"Name" : "djinni",
                "CR"   : "11",
                "Env"  : ["coastal"]},
               {"Name" : "marid",
                "CR"   : "11",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "storm giant",
                "CR"   : "13",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "adult bronze dragon",
                "CR"   : "15",
                "Env"  : ["coastal"]},
               {"Name" : "adult blue dragon",
                "CR"   : "16",
                "Env"  : ["coastal", "desert"]},
               {"Name" : "dragon turtle",
                "CR"   : "17",
                "Env"  : ["coastal", "underwater"]},
               {"Name" : "ancient bronze dragon",
                "CR"   : "22",
                "Env"  : ["coastal"]},
               {"Name" : "ancient blue dragon",
                "CR"   : "23",
                "Env"  : ["coastal", "desert"]},
               {"Name" : "medusa",
                "CR"   : "6",
                "Env"  : ["desert"]},
               {"Name" : "young brass dragon",
                "CR"   : "6",
                "Env"  : ["desert"]},
               {"Name" : "yuan-ti abomination",
                "CR"   : "7",
                "Env"  : ["desert", "forest", "swamp"]},
               {"Name" : "gaurdian naga",
                "CR"   : "10",
                "Env"  : ["desert", "forest"]},
               {"Name" : "efreeti",
                "CR"   : "11",
                "Env"  : ["desert"]},
               {"Name" : "gynosphinx",
                "CR"   : "11",
                "Env"  : ["desert"]},
               {"Name" : "adult brass dragon",
                "CR"   : "13",
                "Env"  : ["desert"]},
               {"Name" : "mummy lord",
                "CR"   : "15",
                "Env"  : ["desert"]},
               {"Name" : "purple worm",
                "CR"   : "15",
                "Env"  : ["desert"]},
               {"Name" : "adult blue dracolich",
                "CR"   : "17",
                "Env"  : ["desert"]},
               {"Name" : "androsphinx",
                "CR"   : "17",
                "Env"  : ["desert"]},
               {"Name" : "ancient brass dragon",
                "CR"   : "20",
                "Env"  : ["desert"]},
               {"Name" : "giant ape",
                "CR"   : "7",
                "Env"  : ["forest"]},
               {"Name" : "grick alpha",
                "CR"   : "7",
                "Env"  : ["forest", "underdark"]},
               {"Name" : "oni",
                "CR"   : "7",
                "Env"  : ["forest", "urban"]},
               {"Name" : "young green dragon",
                "CR"   : "8",
                "Env"  : ["forest"]},
               {"Name" : "treant",
                "CR"   : "9",
                "Env"  : ["forest"]},
               {"Name" : "guardian naga",
                "CR"   : "10",
                "Env"  : ["forest"]},
               {"Name" : "young gold dragon",
                "CR"   : "10",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "adult green dragon",
                "CR"   : "15",
                "Env"  : ["forest"]},
               {"Name" : "adult gold dragon",
                "CR"   : "17",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "ancient green dragon",
                "CR"   : "22",
                "Env"  : ["forest"]},
               {"Name" : "ancient gold dragon",
                "CR"   : "24",
                "Env"  : ["forest", "grassland"]},
               {"Name" : "chimera",
                "CR"   : "6",
                "Env"  : ["grassland", "hill", "mountain", "underdark"]},
               {"Name" : "tyrannosaurus rex",
                "CR"   : "8",
                "Env"  : ["grassland"]},
               {"Name" : "galeb duhr",
                "CR"   : "6",
                "Env"  : ["hill", "mountain"]},
               {"Name" : "wyvern",
                "CR"   : "6",
                "Env"  : ["hill", "mountain"]},
               {"Name" : "stone giant",
                "CR"   : "7",
                "Env"  : ["hill", "mountain", "underdark"]},
               {"Name" : "young copper dragon",
                "CR"   : "7",
                "Env"  : ["hill"]},
               {"Name" : "young red dragon",
                "CR"   : "10",
                "Env"  : ["hill", "mountain"]},
               {"Name" : "adult copper dragon",
                "CR"   : "14",
                "Env"  : ["hill"]},
               {"Name" : "adult red dragon",
                "CR"   : "17",
                "Env"  : ["hill", "mountain"]},
               {"Name" : "ancient copper dragon",
                "CR"   : "21",
                "Env"  : ["hill"]},
               {"Name" : "ancient red dragon",
                "CR"   : "24",
                "Env"  : ["hill", "mountain"]},
               {"Name" : "cloud giant",
                "CR"   : "9",
                "Env"  : ["mountain"]},
               {"Name" : "fire giant",
                "CR"   : "9",
                "Env"  : ["mountain", "underdark"]},
               {"Name" : "young silver dragon",
                "CR"   : "9",
                "Env"  : ["mountain"]},
               {"Name" : "adult silver dragon",
                "CR"   : "16",
                "Env"  : ["mountain"]},
               {"Name" : "ancient silver dragon",
                "CR"   : "23",
                "Env"  : ["mountain"]},
               {"Name" : "young black dragon",
                "CR"   : "7",
                "Env"  : ["swamp"]},
               {"Name" : "hydra",
                "CR"   : "8",
                "Env"  : ["swamp"]},
               {"Name" : "adult black dragon",
                "CR"   : "14",
                "Env"  : ["swamp"]},
               {"Name" : "ancient black dragon",
                "CR"   : "21",
                "Env"  : ["swamp"]},
               {"Name" : "drider",
                "CR"   : "6",
                "Env"  : ["underdark"]},
               {"Name" : "drow mage",
                "CR"   : "7",
                "Env"  : ["underdark"]},
               {"Name" : "mind flayer",
                "CR"   : "8",
                "Env"  : ["underdark"]},
               {"Name" : "arcanist",
                "CR"   : "8",
                "Env"  : ["underdark"]},
               {"Name" : "spirit naga",
                "CR"   : "8",
                "Env"  : ["underdark"]},
               {"Name" : "aboleth",
                "CR"   : "10",
                "Env"  : ["underdark"]},
               {"Name" : "behir",
                "CR"   : "11",
                "Env"  : ["underdark"]},
               {"Name" : "dao",
                "CR"   : "11",
                "Env"  : ["underdark"]},
               {"Name" : "boholder",
                "CR"   : "13",
                "Env"  : ["underdark"]},
               {"Name" : "young red shadow dragon",
                "CR"   : "13",
                "Env"  : ["underdark"]},
               {"Name" : "death tyrant",
                "CR"   : "14",
                "Env"  : ["underdark"]},
               {"Name" : "purple worm",
                "CR"   : "15",
                "Env"  : ["underdark"]},
               {"Name" : "kraken",
                "CR"   : "23",
                "Env"  : ["underwater"]},
               {"Name" : "invisible stalker",
                "CR"   : "6",
                "Env"  : ["urban"]},
               {"Name" : "mage",
                "CR"   : "6",
                "Env"  : ["urban"]},
               {"Name" : "shield guardian",
                "CR"   : "7",
                "Env"  : ["urban"]},
               {"Name" : "assassin",
                "CR"   : "8",
                "Env"  : ["urban"]},
               {"Name" : "gray slaad",
                "CR"   : "9",
                "Env"  : ["urban"]},
               {"Name" : "young silver dragon",
                "CR"   : "9",
                "Env"  : ["urban"]},
               {"Name" : "archmage",
                "CR"   : "12",
                "Env"  : ["urban"]},
               {"Name" : "rakshasa",
                "CR"   : "13",
                "Env"  : ["urban"]},
               {"Name" : "vampire",
                "CR"   : "13",
                "Env"  : ["urban"]},
               {"Name" : "spellcaster vampire",
                "CR"   : "15",
                "Env"  : ["urban"]},
               {"Name" : "warrior vampire",
                "CR"   : "15",
                "Env"  : ["urban"]},
               {"Name" : "adult silver dragon",
                "CR"   : "16",
                "Env"  : ["urban"]},
               {"Name" : "ancient silver dragon",
                "CR"   : "23",
                "Env"  : ["urban"]},
               {"Name" : "tarrasque",
                "CR"   : "30",
                "Env"  : ["urban"]}]


# ------------------- Helpers that build all of the responses ------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# ----------------- Functions that control the skill's behavior ----------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = " Welcome to the Auto D M. " \
                    " How do you want to do this? "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = " What type of monster would you like? " \
                    " You can say Give me a C R 1 moster or " \
                    " Give me a swamp monster. "
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using the Auto D M! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True

    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_monster(monsterCR, monsterEnv):
    # No CR
    if monsterCR == "None":
        monsters = [monster["Name"] for monster
                    in allmonsters
                    if monsterEnv in monster['Env']]
    # No Env
    elif monsterEnv == "None":
        monsters = [monster["Name"] for monster
                    in allmonsters
                    if monster['CR'] == monsterCR]       
    # Both CR and Env
    else:
        monsters = [monster["Name"] for monster
                    in allmonsters
                    if monsterEnv in monster['Env']
                    and monster['CR'] == monsterCR]

    # Get random monster
    if len(monsters):
        monster = random.choice(monsters)
    else:
        monster = "None"

    # Return
    return monster


def monster_by_cr_in_session(intent, session):
    """ Gets a random monster at the specifiecd CR
    """

    card_title = "Monster By CR Return"
    session_attributes = {}
    should_end_session = False
    try:
        monsterCR     = intent['slots']['cr']['value']
    except:
        monsterCR     = "ERROR"

    if monsterCR != "ERROR":
        monsterEnv    = "None"
        monster       = get_monster(monsterCR, monsterEnv)
        speech_output = " A " + \
                        monster + \
                        " attacks! "
        reprompt_text = " Would you like another monster? "
    else:
        speech_output = " I'm not sure what type of monster you want. " \
                        " Please try again. "
        reprompt_text = " I'm not sure what type of monster you want. " \
                        " What type of monster would you like? " \
                        " You can say Give me a C R 1 moster or " \
                        " Give me a swamp monster. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def monster_by_env_in_session(intent, session):
    """ Gets a random monster from the specifiecd environment
    """

    card_title = "Monster By Env Return"
    session_attributes = {}
    should_end_session = False
    try:
        monsterEnv    = intent['slots']['env']['value']
    except:
        monsterEnv    = "ERROR"

    if monsterEnv != "ERROR":
        monsterCR     = "None"
        monsterEnv    = intent['slots']['env']['value']
        monster       = get_monster(monsterCR, monsterEnv)
        speech_output = " A " + \
                        monster + \
                        " attacks! "
        reprompt_text = " Would you like another monster? "
    else:
        speech_output = " I'm not sure what type of monster you want. " \
                        " Please try again. "
        reprompt_text = " I'm not sure what type of monster you want. " \
                        " What type of monster would you like? " \
                        " You can say Give me a C R 1 moster or " \
                        " Give me a swamp monster. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def monster_by_cr_and_env_in_session(intent, session):
    """ Gets a random monster at the specifiecd CR from the specified
    environment
    """

    card_title = "Monster By CR and Env Return"
    session_attributes = {}
    should_end_session = False
    try:
        monsterCR     = intent['slots']['cr']['value']
    except:
        monsterCR     = "ERROR"
    try:
        monsterEnv    = intent['slots']['env']['value']
    except:
        monsterEnv    = "ERROR"

    if monsterCR != "ERROR" and monsterEnv != "ERROR":
        monsterCR     = intent['slots']['cr']['value']
        monsterEnv    = intent['slots']['env']['value']
        monster       = get_monster(monsterCR, monsterEnv)
        if monster != "None":
            speech_output = " A " + \
                            monster + \
                            " attacks! "
        else:
            speech_output = " I'm sorry, no monster matches what you want. "
        reprompt_text = " Would you like another monster? "           
    else:
        speech_output = " I'm not sure what type of monster you want. " \
                        " Please try again. "
        reprompt_text = " I'm not sure what type of monster you want. " \
                        " What type of monster would you like? " \
                        " You can say Give me a C R 1 moster or " \
                        " Give me a swamp monster. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# ----------------------------------- Events -----------------------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MonsterByCRIntent":
        return monster_by_cr_in_session(intent, session)
    elif intent_name == "MonsterByEnvironmentIntent":
        return monster_by_env_in_session(intent, session)
    elif intent_name == "MonsterByCRandEnvironmentIntent":
        return monster_by_cr_and_env_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# -------------------------------- Main handler --------------------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])