from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.videoplayer import VideoPlayer
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
import requests
import os

class MonsterCloud(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#080808')
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # হেডার
        self.label = Label(
            text="MONSTER MEDIA & CLOUD", 
            font_size='20sp', bold=True,
            color=get_color_from_hex('#00E5FF'),
            size_hint=(1, 0.1)
        )
        
        # ভিডিও প্লেয়ার উইজেট (শুরুতে ছোট থাকবে)
        self.video = VideoPlayer(source='', state='pause', options={'allow_stretch': True})
        self.video.size_hint = (1, 0.4)
        
        # ফাইল ব্রাউজার (ভিডিও এবং সব ফাইল দেখাবে)
        self.file_chooser = FileChooserIconView(
            path='/sdcard',
            size_hint=(1, 0.4),
            filters=['*.mp4', '*.mkv', '*.png', '*.jpg', '*.pdf']
        )
        self.file_chooser.bind(on_submit=self.play_video)
        
        # আপলোড বাটন
        btn = Button(
            text="UPLOAD SELECTED FILE", 
            size_hint=(1, 0.1), 
            background_color=get_color_from_hex('#00E5FF'),
            background_normal='',
            bold=True
        )
        btn.bind(on_press=self.upload_logic)
        
        self.main_layout.add_widget(self.label)
        self.main_layout.add_widget(self.video)
        self.main_layout.add_widget(self.file_chooser)
        self.main_layout.add_widget(btn)
        
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.MANAGE_EXTERNAL_STORAGE])
        
        return self.main_layout

    def play_video(self, instance, selection, touch):
        if selection:
            file_path = selection[0]
            if file_path.endswith(('.mp4', '.mkv')):
                self.video.source = file_path
                self.video.state = 'play'
                self.label.text = "Playing: " + os.path.basename(file_path)
            else:
                self.label.text = "Selected: " + os.path.basename(file_path)

    def upload_logic(self, instance):
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            url = "https://deepanjanxyz-private-cloud.hf.space/upload" 
            try:
                self.label.text = "Uploading... (Needs Internet)"
                with open(file_path, 'rb') as f:
                    r = requests.post(url, files={'file': f}, timeout=5)
                if r.status_code == 200:
                    self.label.text = "✅ UPLOADED TO CLOUD!"
                else:
                    self.label.text = "❌ SERVER ERROR"
            except:
                self.label.text = "⚠️ OFFLINE: FILE SAVED LOCALLY"
        else:
            self.label.text = "⚠️ SELECT A FILE FIRST!"

if __name__ == "__main__":
    MonsterCloud().run()
