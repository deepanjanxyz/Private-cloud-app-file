from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import os

# ক্রাশ আটকাতে সেফ ইম্পোর্ট
try:
    from android.permissions import request_permissions, Permission
except ImportError:
    pass

class MonsterCloud(App):
    def build(self):
        # 🌑 ব্যাকগ্রাউন্ড: পিচ কালো (Deep Black)
        Window.clearcolor = get_color_from_hex('#050505')
        
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # 🟢 হ্যাকার স্টাইল হেডার
        self.header = Label(
            text="[b]MONSTER CLOUD[/b] [sub]v2.0[/sub]", 
            markup=True,
            font_size='26sp', 
            color=get_color_from_hex('#00FFCC'), # Neon Cyan
            size_hint=(1, 0.1)
        )
        
        # 📂 ফাইল ম্যানেজার (মডার্ন লুক)
        self.file_chooser = FileChooserIconView(
            path='/sdcard',
            size_hint=(1, 0.7),
            color=get_color_from_hex('#E0E0E0') # Text Color White
        )
        
        # 🚀 আপলোড বাটন (গ্লোয়িং এফেক্ট)
        self.btn = Button(
            text="INITIATE UPLOAD",
            font_size='18sp',
            bold=True,
            size_hint=(1, 0.15),
            background_color=get_color_from_hex('#00E5FF'),
            background_normal='',
            color=get_color_from_hex('#000000') # কালো টেক্সট
        )
        self.btn.bind(on_press=self.on_upload_click)
        
        # 🖥️ স্ট্যাটাস লগ (টার্মিনাল স্টাইল)
        self.status = Label(
            text="> SYSTEM READY...", 
            font_name='Roboto',
            color=get_color_from_hex('#00FF00'), # Matrix Green
            size_hint=(1, 0.05)
        )
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.status)
        
        # 🔐 পারমিশন চাওয়া (অটোমেটিক)
        self.get_permissions()
        
        return self.layout

    def get_permissions(self):
        try:
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.MANAGE_EXTERNAL_STORAGE
            ])
        except Exception:
            self.status.text = "> DEV MODE: No Permissions Needed"

    def on_upload_click(self, instance):
        if self.file_chooser.selection:
            filename = os.path.basename(self.file_chooser.selection[0])
            # ফেক আপলোড প্রসেস (ক্রাশ এড়াতে)
            self.status.text = f"> PROCESSING: {filename}..."
            self.header.text = "[b]SYNCING TO SERVER...[/b]"
            self.btn.background_color = get_color_from_hex('#FF3300') # লাল হয়ে যাবে
        else:
            self.status.text = "> ERROR: NO FILE SELECTED!"

if __name__ == "__main__":
    try:
        MonsterCloud().run()
    except Exception as e:
        print("Crash Prevented")
