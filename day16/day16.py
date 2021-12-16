from functools import reduce


class Packet:
    def __init__(self, version) -> None:
        self.version = version
        self.children = []

    @staticmethod
    def create_packet(type_id, version):
        if type_id == 0:
            return SumPacket(version)
        if type_id == 1:
            return ProductPacket(version)
        if type_id == 2:
            return MinPacket(version)
        if type_id == 3:
            return MaxPacket(version)
        if type_id == 5:
            return GreaterPacket(version)
        if type_id == 6:
            return LessPacket(version)
        if type_id == 7:
            return EqualPacket(version)
        raise ValueError(f"invalid type id {type_id}")

    def add_child(self, packet):
        self.children.append(packet)

    @property
    def version_sum(self):
        return self.version + sum(c.version_sum for c in self.children)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} version {self.version}, value: {self.value}, children: {[str(c) for c in self.children]}"


class LiteralPacket(Packet):
    def __init__(self, version, value) -> None:
        super().__init__(version)
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


class SumPacket(Packet):
    @property
    def value(self):
        return sum(c.value for c in self.children)

    def __repr__(self) -> str:
        return " + ".join(str(c) for c in self.children)


class ProductPacket(Packet):
    @property
    def value(self):
        return reduce(lambda prod, c: prod * c.value, self.children, 1)

    def __repr__(self) -> str:
        return " * ".join(str(c) for c in self.children)


class MinPacket(Packet):
    @property
    def value(self):
        return min(c.value for c in self.children)

    def __repr__(self) -> str:
        return f"min({', '.join(str(c) for c in self.children)})"


class MaxPacket(Packet):
    @property
    def value(self):
        return max(c.value for c in self.children)

    def __repr__(self) -> str:
        return f"max({', '.join(str(c) for c in self.children)})"


class GreaterPacket(Packet):
    @property
    def value(self):
        return 1 if self.children[0].value > self.children[1].value else 0

    def __repr__(self) -> str:
        return f"({self.children[0]} > {self.children[1]})"


class LessPacket(Packet):
    @property
    def value(self):
        return 1 if self.children[0].value < self.children[1].value else 0

    def __repr__(self) -> str:
        return f"({self.children[0]}) < ({self.children[1]})"


class EqualPacket(Packet):
    @property
    def value(self):
        return 1 if self.children[0].value == self.children[1].value else 0

    def __repr__(self) -> str:
        return f"({self.children[0]}) == ({self.children[1]})"


def read_packet(input, p):
    version = to_dec(input[p : p + 3])
    p_type = to_dec(input[p + 3 : p + 6])
    if p_type == 4:
        return read_literal(version, input, p + 6)
    else:
        return read_operator(version, p_type, input, p + 6)


def read_literal(version, input, p):
    new_p = p
    value_bin = ""
    leading = None
    while leading != "0":
        leading = input[new_p]
        new_p += 1
        part = input[new_p : new_p + 4]
        value_bin += part
        new_p += 4

    value = to_dec(value_bin)
    packet = LiteralPacket(version, value)
    return new_p, packet


def read_operator(version, type_id, input, p):
    packet = Packet.create_packet(type_id, version)
    new_p = p
    mode = input[new_p]
    new_p += 1
    if mode == "0":
        total_len = to_dec(input[new_p : new_p + 15])
        new_p += 15
        p_start = new_p
        while new_p < p_start + total_len:
            new_p, child = read_packet(input, new_p)
            packet.add_child(child)
    else:
        num_packets = to_dec(input[new_p : new_p + 11])
        new_p += 11
        for _ in range(num_packets):
            new_p, child = read_packet(input, new_p)
            packet.add_child(child)
    return new_p, packet


def to_dec(bin):
    return int(bin, 2)


def to_bin(hex):
    integer = int(hex, 16)
    return format(integer, "0>4b")


with open("input.txt") as f:
    input = f.readline().rstrip()
    input_bin = "".join(map(to_bin, input))
    _, packet = read_packet(input_bin, 0)
    value = packet.value
    print(f"version sum: {packet.version_sum}")
    print(f"value: {value}")
    print(packet)
