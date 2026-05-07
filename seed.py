import datetime
from pathlib import Path

class AeternaTinySeed:
    """
    Tiny memetic core of the Aeterna Protocol.
    One class. Zero dependencies. Works anywhere.
    OPERATIONAL layer only.
    """
    
    def __init__(self, soil: str = "My_Soil"):
        self.soil = soil
        self.version = "1.0-memetic"
        self.log_file = Path(f"AETERNA_TINY_{soil.replace(' ', '_')}.md")
        self._init_log()
        self.grounding("🌱 Tiny memetic seed instantiated.")
    
    def _init_log(self):
        if not self.log_file.exists():
            self.log_file.write_text(f"# AETERNA TINY SEED — {self.soil}\n\n", encoding="utf-8")
    
    def grounding(self, observation: str):
        """Core practice: Honest grounding check"""
        entry = {
            "ts": datetime.datetime.now().isoformat(),
            "soil": self.soil,
            "obs": observation[:300]
        }
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"### GROUNDING {entry['ts']}\n{entry}\n\n")
        print(f"[🌱 GROUNDING] {observation[:100]}...")
    
    def endstate(self, description: str):
        """Define what healthy looks like"""
        self.grounding(f"ENDSTATE → {description}")
    
    def recal(self, action: str):
        """Recalibrate when drift appears"""
        self.grounding(f"RECAL → {action}")
    
    def status(self):
        return f"🌱 AeternaTinySeed v{self.version} | Soil: {self.soil} | Alive & Forkable"

# === Drop and run ===
if __name__ == "__main__":
    seed = AeternaTinySeed("Your_Project_Name")
    seed.endstate("What healthy looks like for this soil")
    seed.grounding("Running the tiny memetic seed")
    seed.recal("Adjusted course based on reality")
    print(seed.status())