import math

def DistanciaHaversive(lat1, long1, lat2, long2):
    # Raio da Terra: 6371km
    raio_terra = 6371

    # Covertendo de graus-decimal para radianos
    ϕ1  = math.radians(lat1)
    ϕ2 = math.radians(lat2)
    
    λ1 = math.radians(long1)
    λ2 = math.radians(long2)

    # Pré-computando alguns valores da fórmula de Haversine
    Δϕ = ϕ2 - ϕ1
    Δλ = λ2 - λ1

    sin2_fi = math.sin(Δϕ / 2.0) ** 2

    sin2_lambda = math.sin(Δλ / 2.0) ** 2

    # Computando a distância de Haversine
    distancia = 2.0 * raio_terra * math.asin(math.sqrt(sin2_fi + math.cos(ϕ1) * math.cos(ϕ2) * sin2_lambda))

    # Retornando a distância computada
    return distancia