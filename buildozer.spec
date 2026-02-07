[app]
# অ্যাপের নাম ও বেসিক তথ্য
title = Monster Cloud
package.name = monstercloud
package.domain = org.deepanjan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0

# ⚠️ মেইন ফিক্স: শুধু কাজের জিনিস রাখলাম। openssl/requests বাদ।
# এতে বিল্ড টাইম অর্ধেক হয়ে যাবে এবং এরর আসবে না।
requirements = python3,kivy==2.2.1,android,pillow

# স্ক্রিন ও ওরিয়েন্টেশন
orientation = portrait
fullscreen = 0

# পারমিশন (Safe Permissions)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Android API Settings (Standard)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# স্টার্টআপ স্ক্রিন (ইচ্ছা হলে চেঞ্জ করিস)
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

# P4A (Python for Android) কনফিগারেশন
p4a.branch = release-2023.06.16
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
