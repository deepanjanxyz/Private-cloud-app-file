from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
import requests

class MonsterCloudApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Deepanjan's Monster Cloud", font_size='20sp')
        self.file_chooser = FileChooserIconView()
        
        btn = Button(text="Upload to Cloud", size_hint=(1, 0.15), background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.upload_logic)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(btn)
        return self.layout

    def upload_logic(self, instance):
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            # তোর হাগিং ফেস সার্ভারের আপলোড ইউআরএল
            url = "https://deepanjanxyz-private-cloud.hf.space/upload" 
            try:
                self.label.text = "Uploading..."
                files = {'file': open(file_path, 'rb')}
                r = requests.post(url, files=files)
                if r.status_code == 200:
                    self.label.text = "Success: ফাইল পৌঁছে গেছে!"
                else:
                    self.label.text = f"Error: {r.status_code}"
            except Exception as e:
                self.label.text = "Server Connection Failed!"
        else:
            self.label.text = "আগে ফাইল বেছে নে!"

if __name__ == "__main__":
    MonsterCloudApp().run()
