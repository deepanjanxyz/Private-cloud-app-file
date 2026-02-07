[app]
title = Monster Cloud
package.name = monstercloud
package.domain = org.deepanjan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0

# openssl আর sqlite3 যোগ করেছি যাতে নেটওয়ার্ক ও ডেটাবেস নিয়ে সমস্যা না হয়
requirements = python3,kivy==2.2.1,requests,certifi,urllib3,android,openssl

orientation = portrait
fullscreen = 0

# Android specific (API 33 ব্যবহার করা এখন স্ট্যান্ডার্ড)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# আর্কিটেকচার দুটোই রাখলাম যাতে সব ফোনে চলে
android.archs = arm64-v8a, armeabi-v7a

# p4a branch টা স্টেবল রাখছি যাতে বিল্ড ফেইল না হয়
p4a.branch = release-2023.06.16

[buildozer]
log_level = 2
warn_on_root = 1
