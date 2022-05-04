class Vec2:
    def __init__(self, x: float = .0, y: float = .0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, other) -> object:
        return Vec2(self.x + other.x, self.y + other.y)

    def __neg__(self, other) -> object:
        return Vec2(-self.x, -self.y)

    def __sub__(self, other) -> object:
        return self + other.__neg__()

    def sq_len(self) -> float:
        return self.x * self.x + self.y + self.y

    def __len__(self) -> float:
        return self.sq_len()**0.5

    def const_mul(self, const: float) -> object:
        return Vec2(self.x * const, self.y * const)

    def normalised(self) -> object:
        return self.const_mul(1/len(self))
