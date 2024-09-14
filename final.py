from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime, timedelta

class DateCheckerApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical')

        self.label = Label(text='Enter the number of days:')
        self.box.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        self.box.add_widget(self.text_input)

        self.button = Button(text='Calculate Date')
        self.button.bind(on_press=self.calculate_date)
        self.box.add_widget(self.button)

        self.result_label = Label(text='')
        self.box.add_widget(self.result_label)

        return self.box

    def calculate_date(self, instance):
        try:
            

            n = int(self.text_input.text)
            m=n-1
            if m < 0:
                raise ValueError("Number of days cannot be negative.")
            today = datetime.today()
            date_after_n_days = today + timedelta(days=m)
            formatted_date = date_after_n_days.strftime("%d-%m-%Y")
            self.result_label.text = f"The date after {n} days will be: {formatted_date}"
        except ValueError as e:
            self.result_label.text = f"Invalid input: {e}"

if __name__ == '__main__':
    DateCheckerApp().run()
