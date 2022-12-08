class StarCookie:
    milk = 0.1

    def __init__(self, weight=10, color='Red'):
        self.color = color
        self.weight = weight


star_cookie1 = StarCookie()
print(StarCookie.milk)
print(star_cookie1.milk)
print(star_cookie1.__dict__)
print([key for key in StarCookie.__dict__])
