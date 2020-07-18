import googlemaps


class PythonGoogleMaps():
    success_data = []
    failed_data = []
    input_data = None
    gmaps = None
    key = ''

    def __init__(self):
        self.initialize_maps_api()
        self.welcome()
        while True:
            print('Para salir escriba exit')
            self.input_data = input()
            if self.input_data == 'exit':
                break
            self.parse_data()

    def initialize_maps_api(self):
        self.gmaps = googlemaps.Client(
            key=self.key,
        )

    def welcome(self):
        print('come Este es un puzzle de paises')
        print('Debes ingresar ciudad y paises tantos como puedas')
        print('Ejemplo: Cordoba, Argentina')

    def parse_data(self):
        city, country = [var.strip() for var in self.input_data.split(',')]
        geocode_result = self.gmaps.geocode(city)

    @staticmethod
    def get_country_from_json(geocode_result):
        pass


if __name__ == "__main__":
    PythonGoogleMaps()
