import json
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Players:
    token = ''
    high_id = 0
    low_id = 0

    # Brawler data
    #skins_id = Skins.get_skins_id()
    #brawlers_id = Characters.get_brawlers_id()
    #card_skills_id = Cards.get_spg_id()
    #card_unlock_id = Cards.get_brawler_unlock()
    # Brawler data

def __init__(self, device):
    self.device = device