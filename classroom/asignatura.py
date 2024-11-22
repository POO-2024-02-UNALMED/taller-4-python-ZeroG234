class Asignatura:

    def __init__(self, nombre, salon = 0, modalidad = 'remoto'):
        self._nombre = nombre
        self._salon = salon
        self._modalidad = modalidad

    def __str__(self):
        return self._nombre + ' ' + self._modalidad
