from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
import requests
import certifi

class MonsterCloud(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Monster Cloud Drive", font_size='22sp')
        self.file_chooser = FileChooserIconView()
        btn = Button(text="UPLOAD TO SERVER", size_hint=(1, 0.15), background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.upload)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(btn)
        return self.layout

    def upload(self, instance):
        if self.file_chooser.selection:
            path = self.file_chooser.selection[0]
            url = "https://deepanjanxyz-private-cloud.hf.space/upload"
            self.label.text = "Uploading..."
            try:
                files = {'file': open(path, 'rb')}
                r = requests.post(url, files=files, verify=certifi.where())
                if r.status_code == 200:
                    self.label.text = "✅ Success!"
                else:
                    self.label.text = f"❌ Failed: {r.status_code}"
            except Exception as e:
                self.label.text = "⚠️ Connection Error!"
        else:
            self.label.text = "⚠️ Select a file!"

if __name__ == "__main__":
    MonsterCloud().run()
