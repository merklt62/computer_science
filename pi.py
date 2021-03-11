def calculate_pi(n_terms: int) -> float:
    numerator:
        float = 4.0
    denomirator:
        float = 1.0
    operation:
        float = 1.0
    pi:
        float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denomirator)
        denomirator += 2.0
        operation *= -1.0
    return pi

print(calculate_pi(1000000))
