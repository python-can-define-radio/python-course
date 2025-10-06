$documentsPath = [Environment]::GetFolderPath("MyDocuments")
$persistenceRoot = Join-Path $documentsPath "persistence"

# Create persistence Directory
if (-not (Test-Path $persistenceRoot)) {
    New-Item -ItemType Directory -Path $persistenceRoot | Out-Null
    Write-Host "Created persistence root folder: $persistenceRoot"
}

# Create sub directories
$appFolders = @("VSCode", "chrome", "firefox", "msedge", "VSCode/User", "pyinterp", "pyinstall")

foreach ($folder in $appFolders) {
    $fullPath = Join-Path $persistenceRoot $folder
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath | Out-Null
        Write-Host "Created folder: $fullPath"
    }
}

# # The following is based on https://github.com/ethanmartin223/PythonInstaller/blob/main/main.bat
# $pyinst = Join-Path $persistenceRoot "pyinstall"
# curl https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe -OutFile "$pyinst\python-3.8.10.exe"

# Function to simplify shortcut creation
function New-AppShortcut {
    param (
        [string]$targetExe,    # Path to the application executable
        [string]$arguments,     # Command-line arguments to pass to the application
        [string]$shortcutPath   # Where to save the shortcut (.lnk) file
    )

    # Use the Windows Script Host to create a shortcut file
    $shell = New-Object -ComObject WScript.Shell
    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = $targetExe
    $shortcut.Arguments = $arguments
    $shortcut.WorkingDirectory = Split-Path $targetExe  # Set working directory to executable location
    $shortcut.Save()
    Write-Host "Shortcut created: $shortcutPath"
}

$pf64 = [Environment]::GetFolderPath("ProgramFiles")         # Program Files (64-bit)
$pf86 = [Environment]::GetFolderPath("ProgramFilesX86")      # Program Files (x86)

# Create shortcut for Visual Studio Code that uses persistence folders
# Points user data and extensions to persistence and uses custom SSH config
$codeExe = Join-Path $pf64 "Microsoft VS Code\Code.exe"
$codeArgs = "--user-data-dir $persistenceRoot\VSCode --extensions-dir $persistenceRoot\VSCode\extensions"

# Create shortcut for VSCode that uses persistence folder for user data
New-AppShortcut -targetExe $codeExe -arguments $codeArgs -shortcutPath (Join-Path $documentsPath "Persistent VSCode.lnk")

# # Install extensions
# $WantAutoInstall = Read-Host "Install python extension automatically ('a'), or skip (press enter)?"
# if ($WantAutoInstall -eq "a") {
# 	$extensions = @("ms-python.python",)
# 	foreach ($extension in $extensions) {
# 		Write-Host "Installing extension: $extension"
		
# 		# Split arguments into array for Start-Process
# 		$arguments = @(
# 			"--user-data-dir", "$persistenceRoot\VSCode",
# 			"--extensions-dir", "$persistenceRoot\VSCode\extensions", 
# 			"--install-extension", $extension,
# 			"--force",
# 			"--no-sandbox"
# 		)
		
# 		Start-Process -FilePath $codeExe -ArgumentList $arguments -Wait -PassThru -NoNewWindow
# 	}
# } else {
# 	Write-Host "Skipping extension installation; you'll need to do it manually in VS Code."
# }

# Create shortcut for Chrome that uses persistence folder for user data
$chromeExe = Join-Path $pf64 "Google\Chrome\Application\chrome.exe"
$chromeArgs = "--user-data-dir=""$persistenceRoot\chrome"""
New-AppShortcut -targetExe $chromeExe -arguments $chromeArgs -shortcutPath (Join-Path $documentsPath "Launch Chrome.lnk")

# Create shortcut for Edge that uses persistence folder for user data
# Note: There are two methods shown to locate Edge - environment variable and direct path
$edgeExe = Join-Path $pf86 "Microsoft\Edge\Application\msedge.exe"
$edgeArgs = "--user-data-dir=$persistenceRoot\msedge"
New-AppShortcut -targetExe $edgeExe -arguments $edgeArgs -shortcutPath (Join-Path $documentsPath "Launch Edge.lnk")

# Create shortcut for Firefox that uses persistence folder for user profile
$firefoxExe = Join-Path $pf64 "Mozilla Firefox\firefox.exe"
$firefoxArgs = "-profile ""$persistenceRoot\firefox"""
New-AppShortcut -targetExe $firefoxExe -arguments $firefoxArgs -shortcutPath (Join-Path $documentsPath "Launch Firefox.lnk")


# # create VSCode/User/settings.json
# $settingsPath = Join-Path $persistenceRoot "VSCode/User/settings.json"
# if (-not (Test-Path $settingsPath)) {
#     $settingsContent | Out-File -FilePath $settingsPath -Encoding UTF8
#     Write-Host "Created VSCode settings.json: $settingsPath"
# }
Write-Host "-----------------------------------"
Write-Host "In order to save your settings between days,"
Write-Host "you'll need to use the shortcuts that are located in Documents."
