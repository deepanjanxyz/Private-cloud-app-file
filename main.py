from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
import requests

class MonsterCloud(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Deepanjan's Monster Cloud", font_size='22sp', color=(0, 1, 1, 1))
        
        # ফাইল চুজ করার উইন্ডো
        self.file_chooser = FileChooserIconView()
        
        # আপলোড বাটন
        btn = Button(text="UPLOAD TO 16GB CLOUD", size_hint=(1, 0.15), background_color=(0, 0.5, 1, 1), font_size='18sp')
        btn.bind(on_press=self.start_upload)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(btn)
        return self.layout

    def start_upload(self, instance):
        if self.file_chooser.selection:
            path = self.file_chooser.selection[0]
            filename = path.split('/')[-1]
            # তোর হাগিং ফেস সার্ভারের ডাইরেক্ট API লিঙ্ক
            url = "https://deepanjanxyz-private-cloud.hf.space/upload"
            
            self.label.text = f"Uploading: {filename}..."
            try:
                with open(path, 'rb') as f:
                    r = requests.post(url, files={'file': f}, timeout=30)
                if r.status_code == 200:
                    self.label.text = "✅ Success! ফাইলে পৌঁছে গেছে।"
                else:
                    self.label.text = f"❌ Error: {r.status_code}"
            except Exception as e:
                self.label.text = "⚠️ Connection Failed!"
        else:
            self.label.text = "⚠️ আগে একটা ফাইল বেছে নে!"

if __name__ == "__main__":
    MonsterCloud().run()
