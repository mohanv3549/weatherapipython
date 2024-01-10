import requests
import os
import json
city=input("enter the name of city:")
url=f'https://api.weatherapi.com/v1/current.json?key=e7fd9006e4244df7b5f112028240601&q={city}%27'
r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
newdic={wdic["current"]["last_updated"],wdic["current"]["temp_c"]}
print(newdic)
x=wdic["current"]["last_updated"]
y=wdic["current"]["temp_c"]
command=f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
command1=f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{y}\')"'
command2=f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'whether report of {city}\')"'
os.system(command2)
os.system('powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'last updated time\')')
os.system(command)
os.system('powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'and the temperature is\')')
os.system(command1)