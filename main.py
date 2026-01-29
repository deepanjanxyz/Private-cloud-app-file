from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import os

# অ্যান্ড্রয়েড পারমিশন ও ক্রাশ হ্যান্ডেলিং
try:
    from android.permissions import request_permissions, Permission
except ImportError:
    pass

class MonsterCloud(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#0A0A0A') # ডার্ক গেমিং লুক
        self.main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # স্টাইলিশ হেডার
        self.label = Label(
            text="MONSTER CLOUD DRIVE [PRO]", 
            font_size='22sp', bold=True,
            color=get_color_from_hex('#00E5FF'),
            size_hint=(1, 0.1)
        )
        
        # ফাইল ম্যানেজার (সব ফোন সাপোর্ট করবে)
        self.file_chooser = FileChooserIconView(
            path='/sdcard',
            size_hint=(1, 0.75),
            color=get_color_from_hex('#FFFFFF')
        )
        
        # আপলোড বাটন
        self.up_btn = Button(
            text="UPLOAD TO SERVER", 
            size_hint=(1, 0.15), 
            background_color=get_color_from_hex('#00E5FF'),
            background_normal='',
            color=(0,0,0,1),
            bold=True,
            font_size='18sp'
        )
        self.up_btn.bind(on_press=self.safe_upload)
        
        self.main_layout.add_widget(self.label)
        self.main_layout.add_widget(self.file_chooser)
        self.main_layout.add_widget(self.up_btn)
        
        # সব ফোনের জন্য পারমিশন রিকোয়েস্ট
        try:
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE, 
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.MANAGE_EXTERNAL_STORAGE
            ])
        except Exception as e:
            print(f"Permission Error: {e}")
            
        return self.main_layout

    def safe_upload(self, instance):
        # ক্রাশ হ্যান্ডেলিং সহ আপলোড লজিক
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            self.label.text = "Attempting: " + os.path.basename(file_path)
            
            # এখানে আমরা ফিউচারে সার্ভার লজিক অ্যাড করবো
            # আপাতত অফলাইন ক্রাশ চেক করার জন্য এই মেসেজ
            self.label.text = "✅ File Selected. Server Sync Pending..."
        else:
            self.label.text = "⚠️ Please select a file first!"

if __name__ == "__main__":
    try:
        MonsterCloud().run()
    except Exception as e:
        # অ্যাপ যেন হঠাৎ বন্ধ না হয়
        print(f"App Crash Protected: {e}")
