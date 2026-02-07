import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.progressbar import ProgressBar
from kivy.utils import get_color_from_hex, platform
from kivy.core.window import Window
from kivy.clock import Clock, mainthread

class MonsterCloud(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#050505')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # হেডার
        self.header = Label(
            text="[b]MONSTER CLOUD[/b] [sub]v3.0[/sub]", 
            markup=True, font_size='28sp', 
            color=get_color_from_hex('#00FFCC'), size_hint=(1, 0.1)
        )
        
        # স্মার্ট পাথ
        root_path = '/sdcard' if platform == 'android' else os.path.expanduser("~")
        
        self.file_chooser = FileChooserIconView(
            path=root_path, size_hint=(1, 0.6),
            color=get_color_from_hex('#E0E0E0')
        )
        
        self.progress = ProgressBar(max=100, value=0, size_hint=(1, 0.05), opacity=0)
        
        self.btn = Button(
            text="INITIATE UPLOAD", font_size='20sp', bold=True,
            size_hint=(1, 0.15), background_normal='',
            background_color=get_color_from_hex('#00E5FF'),
            color=(0,0,0,1)
        )
        self.btn.bind(on_press=self.start_upload)
        
        self.status = Label(text="> SYSTEM READY", color=(0,1,0,1), size_hint=(1, 0.1))
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(self.progress)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.status)
        
        if platform == 'android':
            Clock.schedule_once(self.get_permissions, 1)
            
        return self.layout

    def get_permissions(self, dt):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except:
            self.status.text = "> PERMISSION BYPASS (DEV MODE)"

    def start_upload(self, instance):
        if self.file_chooser.selection:
            self.btn.disabled = True
            self.progress.opacity = 1
            threading.Thread(target=self.fake_upload).start()
        else:
            self.status.text = "> ERROR: NO FILE SELECTED"

    def fake_upload(self):
        import time
        for i in range(101):
            time.sleep(0.03)
            self.update_ui(i)
        self.complete()

    @mainthread
    def update_ui(self, val):
        self.progress.value = val
        self.status.text = f"> UPLOADING... {val}%"

    @mainthread
    def complete(self):
        self.status.text = "> UPLOAD COMPLETE!"
        self.btn.disabled = False
        self.progress.opacity = 0

if __name__ == "__main__":
    MonsterCloud().run()
        
