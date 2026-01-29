from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
import requests
import certifi

class MonsterCloud(App):
    def build(self):
        # ব্যাকগ্রাউন্ড কালার ডার্ক করা
        Window.clearcolor = get_color_from_hex('#121212')
        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # হেডার
        self.label = Label(
            text="MONSTER CLOUD DRIVE", 
            font_size='24sp', 
            bold=True,
            color=get_color_from_hex('#00E5FF'),
            size_hint=(1, 0.1)
        )
        
        # ফাইল ব্রাউজার (একটু স্টাইলিশ)
        self.file_chooser = FileChooserIconView(
            path='/sdcard', 
            size_hint=(1, 0.7)
        )
        
        # আপলোড বাটন (কালারফুল)
        btn = Button(
            text="UPLOAD TO CLOUD", 
            size_hint=(1, 0.15), 
            background_color=get_color_from_hex('#00E5FF'),
            background_normal='',
            font_size='20sp',
            bold=True
        )
        btn.bind(on_press=self.upload_logic)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(btn)
        
        # অ্যান্ড্রয়েড পারমিশন রিকোয়েস্ট
        try:
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except:
            pass
            
        return self.layout

    def upload_logic(self, instance):
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            url = "https://deepanjanxyz-private-cloud.hf.space/upload" 
            self.label.text = "Uploading..."
            try:
                files = {'file': open(file_path, 'rb')}
                r = requests.post(url, files=files, verify=certifi.where())
                if r.status_code == 200:
                    self.label.text = "✅ SUCCESS: UPLOADED!"
                else:
                    self.label.text = f"❌ ERROR: {r.status_code}"
            except Exception as e:
                self.label.text = "⚠️ CONNECTION FAILED!"
        else:
            self.label.text = "⚠️ SELECT A FILE FIRST!"

if __name__ == "__main__":
    MonsterCloud().run()
