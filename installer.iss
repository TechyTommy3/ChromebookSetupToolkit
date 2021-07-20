[Setup]
DisableWelcomePage=False
AppName=Chromebook Switching Kit
AppVersion=0.0.1
AppId={{87DCB818-862C-46BA-B886-27298ACEDB37}
InfoBeforeFile=userdocs:My Python Code\Chromebook Setup Toolkit\Installer\warning.txt
DefaultDirName=C:\Program Files\Chromebook Switching Kit
DefaultGroupName=TechyTommy
UninstallDisplayName=Chromebook Switching Kit
MinVersion=0,6.2
SetupIconFile=userdocs:My Python Code\Chromebook Setup Toolkit\Installer\87865_chrome_icon.ico

[Files]
Source: "Files\main.py"; DestDir: "{app}"; Flags: ignoreversion
