@echo off
::change directory "XXX" to local project directory
:: replace with the directory where you've cloned the repo
pushd "C:\Users\jodoe\projects\Discord-Automation\"
:: execute batch python main file - edit this is your python install is located elsewhere
start "" "C:\Program Files\Python39\python.exe" main.py
:: change directory back
popd
:: run elden ring
start "" "C:\Program Files (x86)\Steam\steam.exe" steam://rungameid/1245620