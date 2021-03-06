"""
Clase que contiene la estructura para la ejecuccion del algoritmo LLE para diferentes datos dado el número de componentes y perplejidad
"""

from sklearn.manifold import LocallyLinearEmbedding
from numpy import array


class LLE_model:
    def __init__(self) -> None:
        pass

    def create(self, n_components: int, neighbors: int) -> None:
        """
        Inicializa el algortimo LLE dado el numero de componentes y el nombre del kernel
        """
        self.model = LocallyLinearEmbedding(n_components=n_components,
                                            n_neighbors=neighbors)
        self.generate_header_names(n_components)

    def run(self, data: array) -> None:
        """
        Ejecuta el algortimo LLE dado un embedding
        """
        self.results = self.model.fit_transform(data)

    def generate_header_names(self, n_components: int) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        name = "Component {}"
        self.names = [name.format(i+1)
                      for i in range(n_components)]

    def get_results(self) -> array:
        """
        Resultados del la ejecucción del modelo
        """
        return self.results.copy()
