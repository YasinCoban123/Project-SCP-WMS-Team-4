from datetime import datetime

class Base:
    def __init__():
        pass

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"  # tijd in UTC-formaat met 'Z' aan het einde om aan te geven dat het in UTC is