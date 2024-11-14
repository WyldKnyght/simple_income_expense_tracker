from datetime import datetime

class Transaction:
    def __init__(self, id=None, date=None, description="", amount=0.0, type="expense"):
        self.id = id
        self.date = date or datetime.now()
        self.description = description
        self.amount = amount
        self.type = type

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "description": self.description,
            "amount": self.amount,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            date=datetime.fromisoformat(data["date"]),
            description=data["description"],
            amount=data["amount"],
            type=data["type"]
        )