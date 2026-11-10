class Vehiculo:
    """Molde que representa un vehículo eléctrico en el simulador municipal."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float):
        self.matricula: str = matricula
        self.modelo: str = modelo
        self.capacidad_kwh: float = capacidad_kwh
        self.nivel_bateria: float = 100.0
        self.kilometros_totales: float = 0.0

    def conducir(self, distancia_km: float) -> bool:
        """Simula un trayecto urbano. Consume 0.15 kWh por cada km recorrido."""
        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (energia_necesaria / self.capacidad_kwh) * 100.0

        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self.kilometros_totales += distancia_km
            return True
        else:
            return False

    def obtener_estado(self) -> str:
        """Devuelve una ficha legible con la telemetría del vehículo."""
        return f"[{self.matricula}] {self.modelo} | Batería: {self.nivel_bateria:.1f}% | Total: {self.kilometros_totales} km"

    def recargar(self, energia_kwh: float) -> float:
        porcentaje_recarga = (energia_kwh / self.capacidad_kwh) * 100.0
        porcentaje_recarga = porcentaje_recarga + self.nivel_bateria
        if porcentaje_recarga > 100.0:
            porcentaje_recarga = 100.0
        return self.nivel_bateria