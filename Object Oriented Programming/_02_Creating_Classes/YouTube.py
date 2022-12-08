class YouTube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


u1 = YouTube('Vamshi')
u2 = YouTube('Bhargavi')
u1.subscribe(u2)

print(u1.subscriptions)
print(u1.subscribers)
print(u2.subscriptions)
print(u2.subscribers)
