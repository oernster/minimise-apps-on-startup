# MinimiseAppsOnStartup
Minimise all windows applications launched during startup.  Works on Windows 11.
Depending on your startup time, you may need to adjust TIMER_VAL in config.json; currently it's set to 10 seconds.
If you want to bundle this into an executable, do the following:

Firstly install Python 3.  I used Python 3.9.7 but I strongly suspect earlier versions as long as they are at least a fairly recent version of Python 3 would be fine.
Install virtualenv
Clone the repo.
Navigate to the repo directory.
run 'virtualenv venv'
run 'venv\Scripts\activate'
run 'pip install -r requirements.txt'
run 'pyinstaller MinimiseAppsOnStartup.py'

This will create a dist directory in your repo directory.
Copy the config.json file into the '<repo dir>\dist\MinimiseAppsOnStartup' directory. 
Copy the entirety of the MinimiseAppsOnStartup directory contained within the dist directory (not dist itself) into c:\program files (x86) (you may need to have admin priviledges for this operation).

Press windows key + r and type in 'shell:startup'
Insert all programs not already integrated into windows 11's personalisation control panel settings that you want as shortcuts.
Create a shortcut for the target 'c:\program files (x86)\MinimiseAppsOnStartup\MinimiseAppsOnStartup.exe' and put it in the shell:startup directory.

Reboot!
