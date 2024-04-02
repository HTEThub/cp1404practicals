from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        """ Builds the app so the layouts can appear on screen """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """ Handles the calculation of input miles to km"""
        value = float(self.validate_miles())
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """ Handles incrementing of the input miles when up/down button is pressed """
        value = self.validate_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def validate_miles(self):
        """ Error-check the input miles to only be numbers/floats """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
