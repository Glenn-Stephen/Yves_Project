import json
import toutes_les_classes
import fonctions_pour_les_classes

chemin = r"C:\Users\Glenn\Script_Yves\projet_python\Data_base.json"
with open(chemin, "r", encoding='utf-8') as f:
    data_base = json.load(f)
    

fonctions_pour_les_classes.display_data_base(data_base)

