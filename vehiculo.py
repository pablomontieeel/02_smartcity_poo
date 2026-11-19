class Vehiculo:
    """Molde que representa un vehículo eléctrico en el simulador municipal."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float):
        self.matricula: str = matricula
        self.modelo: str = modelo
        self.capacidad_kwh: float = capacidad_kwh
        self.nivel_bateria: float = 100.0
        self._kilometros_totales: float = 0.0
    @property
    def kilometros_totales(self) -> float:
        return self._kilometros_totales
    
    @kilometros_totales.setter
    def kilometros_totales(self, nuevos_km: float) -> None:
        if nuevos_km < self._kilometros_totales:
            raise ValueError("Los kilómetros no pueden disminuir (fraude de odómetro).")
        else:
            self._kilometros_totales = nuevos_km

    def conducir(self, distancia_km: float) -> bool:
        """Simula un trayecto urbano. Consume 0.15 kWh por cada km recorrido."""
        self.kilometros_totales = self.kilometros_totales + distancia_km
        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (energia_necesaria / self.capacidad_kwh) * 100.0

        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self._kilometros_totales = self._kilometros_totales + distancia_km
            return True
        else:
            return False

    def obtener_estado(self) -> str:
        """Devuelve una ficha legible con la telemetría del vehículo."""
        return f"[{self.matricula}] {self.modelo} | Batería: {self.nivel_bateria:.1f}% | Total: {self._kilometros_totales} km"

    def recargar(self, energia_kwh: float) -> float:
        porcentaje_recarga = (energia_kwh / self.capacidad_kwh) * 100.0
        self.nivel_bateria = porcentaje_recarga + self.nivel_bateria
        if self.nivel_bateria > 100.0:
            self.nivel_bateria = 100.0
        return self.nivel_bateria