
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
nltk.download('vader_lexicon')

class Processor:
    @staticmethod
    def PEmotions_of_text(df):
        df["sentiment"]=df["Text"].apply(Processor.Emotions_of_text)
        return df

    @staticmethod
    def Emotions_of_text(tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        answer=""
        if score["compound"] >= 0.5:
            answer= "Positive"
        elif score["compound"] <= -0.5:
            answer= "Negative"
        else:
            answer= "Neutral"
        return answer

    # =================================

    @staticmethod
    def PFinding_the_rarest_word(df):
        df["rarest_word"] = df["Text"].apply(Processor.find_rasrest_word)
        return df
    @staticmethod
    def find_rasrest_word(text):
        words = text.split()
        if not words:
            return None
        counts = Counter(words)
        min_freq = min(counts.values())
        rarest = [w for w, c in counts.items() if c == min_freq]
        return rarest[0]

    # =================================

    @staticmethod
    def Pweapon_find(df):
        df["weapons_detected"]=df["Text"].apply(Processor.weapon_find)
        return df
    @staticmethod
    def weapon_find(text):
        # weapons =Processor.load_txt()
        weapons=[
            "A-bomb",
            "ammo",
            "ammunition",
            "armaments",
            "arms",
            "arrow",
            "assault rifle",
            "atom bomb",
            "atomic bomb",
            "autocannon",
            "automatic rifle",
            "axe",
            "ballista",
            "ballistic missile",
            "bat",
            "baton",
            "battle axe",
            "bayonet",
            "bazooka",
            "billy club",
            "biological weapon",
            "blackjack",
            "blade",
            "blaster",
            "blowgun",
            "blowpipe",
            "bludgeon",
            "bomb",
            "boobytrap",
            "boomerang",
            "bow and arrow",
            "Bowie knife",
            "brass knuckles",
            "bullet",
            "bullwhip",
            "cannon",
            "carbine",
            "cat o'nine tails",
            "catapult",
            "cleaver",
            "club",
            "crossbow",
            "cudgel",
            "cutlass",
            "dagger",
            "dart",
            "depth charge",
            "epee",
            "explosives",
            "firearm",
            "flail",
            "flamethrower",
            "flintlock",
            "foil",
            "Gatling gun",
            "grenade",
            "grenade launcher",
            "guided missile",
            "gun",
            "gunpowder",
            "halberd",
            "hand grenade",
            "handgun",
            "harpoon",
            "hatchet",
            "howitzer",
            "hunting knife",
            "javelin",
            "katana",
            "knife",
            "knout",
            "kris",
            "lance",
            "landmine",
            "longbow",
            "longsword",
            "mace",
            "machete",
            "machine gun",
            "magnum",
            "maul",
            "mine",
            "missile",
            "morning star",
            "mortar",
            "munitions",
            "musket",
            "mustard gas",
            "muzzleloader",
            "nerve gas",
            "night stick",
            "nuclear bomb",
            "nunchaku (nunchucks)",
            "onager",
            "ordnance",
            "peashooter",
            "pepper spray",
            "pickaxe",
            "pike",
            "pistol",
            "pommel",
            "quarterstaff",
            "rapier",
            "revolver",
            "rifle",
            "rocket",
            "rocket launcher",
            "saber",
            "scimitar",
            "scythe",
            "semiautomatic",
            "shell",
            "shillelagh",
            "shooter",
            "shotgun",
            "sickle",
            "slingshot",
            "spear",
            "spiked mace",
            "stiletto",
            "stun gun",
            "submachine gun",
            "switchblade",
            "sword",
            "tank",
            "tank gun",
            "taser",
            "tear gas",
            "tomahawk",
            "torpedo",
            "trebuchet",
            "trident",
            "tripwire",
            "truncheon",
            "uzi",
            "weapon",
            "weapon of mass destruction",
            "weaponry",
            "whip"
        ]
        words = text.split()

        for word in words:
            if word in weapons:
                print("3333")
                return word
        return "---"
    # =================================

    # @staticmethod
    # def load_txt():
    #     with open("../data/weapon_list.txt", "r") as text_file:
    #         lines = [line.strip() for line in text_file.readlines()]
    #     return lines

# print(Processor.load_txt())