class MockDB:
    def __init__(self):
        self.data = [
            {
                "id": 1,
                "first_name": "Peter",
                "last_name": "Parker",
                "nickname": "spider-man",
                "universe": "MARVEL",
            },
            {
                "id": 2,
                "first_name": "Bruce",
                "last_name": "Banner",
                "nickname": "hulk",
                "universe": "MARVEL",
            },
            {
                "id": 3,
                "first_name": "Steve",
                "last_name": "Roger",
                "nickname": "captain-america",
                "universe": "MARVEL",
            },
            {
                "id": 4,
                "first_name": "Tony",
                "last_name": "Stark",
                "nickname": "iron-man",
                "universe": "MARVEL",
                "universe": "MARVEL",
            },
            {
                "id": 5,
                "first_name": "Carol",
                "last_name": "Danvers",
                "nickname": "captain-marvel",
                "universe": "MARVEL",
            },
            {
                "id": 6,
                "first_name": "Son",
                "last_name": "Goku",
                "nickname": "goku",
                "universe": "OTHER",
            },
        ]

    def save(hero: dict):
        self.data(hero)

    def update(hero_updated: dict):
        for index, hero in enumerate(self.data):
            if hero["id"] == hero_updated["id"]:
                self.data[index] = hero_updated

    def find_all():
        return self.data

    def find_by_id(id: str):
        for hero in self.data:
            if hero["id"] == id:
                return hero

    def delete(id: str):
        for index, hero in enumerate(self.data):
            if hero["id"] == id:
                del self.data[index]
