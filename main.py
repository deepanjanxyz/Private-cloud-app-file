from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import requests
import certifi
import os

# অ্যান্ড্রয়েড স্পেসিফিক মডিউল
from android.permissions import request_permissions, Permission

class MonsterCloud(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#121212')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.label = Label(
            text="MONSTER CLOUD DRIVE", 
            font_size='22sp', 
            bold=True,
            color=get_color_from_hex('#00E5FF'),
            size_hint=(1, 0.1)
        )
        
        # ফাইল চুজারে সরাসরি /sdcard পাথ সেট করা
        self.file_chooser = FileChooserIconView(
            path='/sdcard',
            size_hint=(1, 0.7)
        )
        
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
        
        # অ্যাপ খুললেই পারমিশন চাইবে
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE, 
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.MANAGE_EXTERNAL_STORAGE
        ])
        
        return self.layout

    def upload_logic(self, instance):
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            url = "https://deepanjanxyz-private-cloud.hf.space/upload" 
            self.label.text = "Attempting Upload..."
            
            try:
                # সার্ভার বন্ধ থাকলেও যেন অ্যাপ না ফাটে তার জন্য Try-Except
                with open(file_path, 'rb') as f:
                    files = {'file': f}
                    r = requests.post(url, files=files, verify=certifi.where(), timeout=10)
                    
                if r.status_code == 200:
                    self.label.text = "✅ SUCCESS: UPLOADED!"
                else:
                    self.label.text = f"❌ SERVER ISSUE: {r.status_code}"
            except Exception as e:
                # সার্ভার বন্ধ থাকলে এই মেসেজ দেখাবে
                self.label.text = "⚠️ SERVER DOWN / NO INTERNET"
        else:
            self.label.text = "⚠️ SELECT A FILE FIRST!"

if __name__ == "__main__":
    MonsterCloud().run()
