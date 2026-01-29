from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import os

class MonsterCloud(App):
    def build(self):
        # কালো ব্যাকগ্রাউন্ড
        Window.clearcolor = get_color_from_hex('#0A0A0A')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="MONSTER CLOUD DRIVE", font_size='20sp', color=(0, 1, 1, 1), size_hint=(1, 0.1))
        
        # একদম বেসিক ফাইল ব্রাউজার (ক্রাশ প্রোটেক্টেড)
        self.chooser = FileChooserIconView(path='/sdcard', size_hint=(1, 0.8))
        
        btn = Button(text="UPLOAD FILE", size_hint=(1, 0.1), background_color=(0, 0.8, 0.8, 1))
        btn.bind(on_release=self.check_file)
        
        layout.add_widget(self.label)
        layout.add_widget(self.chooser)
        layout.add_widget(btn)
        return layout

    def check_file(self, instance):
        if self.chooser.selection:
            self.label.text = "Selected: " + os.path.basename(self.chooser.selection[0])
        else:
            self.label.text = "Please Select a File First!"

if __name__ == "__main__":
    MonsterCloud().run()
