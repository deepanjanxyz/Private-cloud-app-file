import os
import time
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex, platform
from kivy.core.window import Window
from kivy.clock import Clock, mainthread

# 🎨 কালার প্যালেট (Hacker Theme)
COLOR_BG = '#050505'       # পিচ কালো
COLOR_ACCENT = '#00FFCC'   # নিওন সায়ান
COLOR_TEXT = '#E0E0E0'     # সাদা টেক্সট
COLOR_BTN = '#00E5FF'      # বাটন কালার
COLOR_WARN = '#FF3300'     # ওয়ার্নিং রেড
COLOR_SUCCESS = '#00FF00'  # হ্যাকার গ্রিন

# ক্রাশ আটকাতে সেফ ইম্পোর্ট (Android এর জন্য)
try:
    from android.permissions import request_permissions, Permission
except ImportError:
    pass

class MonsterCloud(App):
    def build(self):
        # 🌑 ব্যাকগ্রাউন্ড সেটআপ
        Window.clearcolor = get_color_from_hex(COLOR_BG)
        
        # মেইন লেআউট
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 🟢 হ্যাকার স্টাইল হেডার
        self.header = Label(
            text="[b]MONSTER CLOUD[/b] [sub]v3.0[/sub]", 
            markup=True,
            font_size='28sp', 
            color=get_color_from_hex(COLOR_ACCENT),
            size_hint=(1, 0.1)
        )
        
        # 📂 স্মার্ট পাথ ডিটেকশন (পিসি ও মোবাইল দুই জায়গাতেই কাজ করবে)
        root_path = '/sdcard' if platform == 'android' else os.path.expanduser("~")
        
        # ফাইল ম্যানেজার
        self.file_chooser = FileChooserIconView(
            path=root_path,
            size_hint=(1, 0.6),
            color=get_color_from_hex(COLOR_TEXT)
        )
        
        # 📊 প্রগ্রেস বার (নতুন ফিচার)
        self.progress = ProgressBar(max=100, value=0, size_hint=(1, 0.05))
        self.progress.opacity = 0 # শুরুতে লুকিয়ে থাকবে
        
        # 🚀 আপলোড বাটন
        self.btn = Button(
            text="INITIATE UPLOAD",
            font_size='20sp',
            bold=True,
            size_hint=(1, 0.15),
            background_normal='',
            background_color=get_color_from_hex(COLOR_BTN),
            color=get_color_from_hex('#000000')
        )
        self.btn.bind(on_press=self.start_upload_thread)
        
        # 🖥️ স্ট্যাটাস লগ
        self.status = Label(
            text="> SYSTEM READY... WAITING FOR INPUT", 
            font_name='Roboto',
            color=get_color_from_hex(COLOR_SUCCESS),
            size_hint=(1, 0.1)
        )
        
        # উইজেটগুলো অ্যাড করা
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(self.progress) # প্রগ্রেস বার মাঝখানে দিলাম
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.status)
        
        # 🔐 পারমিশন (Android হলে)
        if platform == 'android':
            self.get_permissions()
            
        return self.layout

    def get_permissions(self):
        try:
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])
        except Exception:
            self.status.text = "> DEV MODE: No Permissions Context"

    # 🧵 মাল্টি-থ্রেডিং: যাতে অ্যাপ হ্যাং না করে
    def start_upload_thread(self, instance):
        if not self.file_chooser.selection:
            self.show_popup("Error", "No File Selected!")
            self.status.text = "> ERROR: TARGET NOT FOUND!"
            self.status.color = get_color_from_hex(COLOR_WARN)
            return

        # বাটন ডিসেবল করে দেব যাতে বারবার চাপ না দেয়
        self.btn.disabled = True
        self.btn.text = "UPLOADING..."
        self.progress.opacity = 1
        
        # ব্যাকগ্রাউন্ডে কাজ শুরু
        threading.Thread(target=self.simulate_upload_process).start()

    # 🔄 ফেক আপলোড প্রসেস (রিয়েলিস্টিক সিমুলেশন)
    def simulate_upload_process(self):
        filename = os.path.basename(self.file_chooser.selection[0])
        self.update_status(f"> ENCRYPTING & UPLOADING: {filename}", COLOR_ACCENT)
        
        for i in range(1, 101):
            time.sleep(0.05) # নেটওয়ার্ক ডিলে সিমুলেশন
            self.update_progress(i)
        
        self.upload_complete()

    # 🖥️ UI আপডেট ফাংশন (মেইন থ্রেড থেকে কল হবে)
    @mainthread
    def update_progress(self, value):
        self.progress.value = value

    @mainthread
    def update_status(self, text, color_hex):
        self.status.text = text
        self.status.color = get_color_from_hex(color_hex)

    @mainthread
    def upload_complete(self):
        self.status.text = "> UPLOAD SUCCESSFUL! SERVER SYNCED."
        self.status.color = get_color_from_hex(COLOR_SUCCESS)
        self.btn.disabled = False
        self.btn.text = "INITIATE UPLOAD"
        self.progress.value = 0
        self.progress.opacity = 0
        self.show_popup("Success", "File uploaded to Monster Cloud!")

    # 🔔 পপআপ মেসেজ দেখানোর জন্য
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        btn = Button(text="OK", size_hint=(1, 0.25))
        popup = Popup(title=title, content=content, size_hint=(None, None), size=(300, 200))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()

if __name__ == "__main__":
    try:
        MonsterCloud().run()
    except Exception as e:
        print(f"Crash Report: {e}")
        
