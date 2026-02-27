[app]

title = Signal App
package.name = signalapp
package.domain = org.signal

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET
android.build_tools_version = 33.0.2
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21
