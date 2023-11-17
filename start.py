import subprocess
import os

os.system(f"title AV SCAN 2023")

def check_system_architecture():
    system_drive = os.environ['SystemDrive']
    program_files = os.path.join(system_drive, 'Program Files')
    
    if os.path.exists(program_files + ' (x86)'):
        system = "x64"
        npe_link = "https://www.norton.com/npe_latest"
        adv_link = "https://adwcleaner.malwarebytes.com/adwcleaner?channel=release"
        KVRT_link = "https://devbuilds.s.kaspersky-labs.com/devbuilds/KVRT/latest/full/KVRT.exe"
    else:
        system = "x32"
        npe_link = "https://www.norton.com/npe_x86"
        adv_link = "https://adwcleaner.malwarebytes.com/adwcleaner?channel=release"
        KVRT_link = "https://devbuilds.s.kaspersky-labs.com/devbuilds/KVRT/latest/full/KVRT.exe"
    
    return system, npe_link, adv_link, KVRT_link

def download_anti():
    system, npe_link, adv_link, KVRT_link = check_system_architecture()
    
    try:
        if not os.path.exists(f"NPE.exe"):
            command1 = f'powershell -Command "Invoke-WebRequest -Uri \\"{npe_link}\\" -OutFile NPE.exe"'
            subprocess.run(command1, shell=True, check=True)
        else:
            pass
        if not os.path.exists(f"adwcleaner.exe"):
            command2 = f'powershell -Command "Invoke-WebRequest -Uri \\"{adv_link}\\" -OutFile adwcleaner.exe"'
            subprocess.run(command2, shell=True, check=True)
        else:
            pass
        if not os.path.exists(f"KVRT.exe"):
            command3 = f'powershell -Command "Invoke-WebRequest -Uri \\"{KVRT_link}\\" -OutFile KVRT.exe"'
            subprocess.run(command3, shell=True, check=True)
        else:
            pass
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_antivirus_scans():
    kvrt_command = "KVRT.exe -accepteula -silent"
    adv_command = "adwcleaner.exe /scan /eula /clean /noreboot"
    NPE = "NPE.exe"
    n = """takeown /f "C:\KVRT2020_Data" /r /d y"""
    l = """takeown /f "C:\AdwCleaner" /r /d y"""

    try:
        kvrt_process = subprocess.Popen(kvrt_command, shell=True)
        kvrt_process.wait()
        print("Kaspersky scan completed.")

        ADV_procces = subprocess.Popen(adv_command, shell=True)
        print("AD WARE scan completed.")

        print("Click on Scan now or skanuj teraz")
        print("after this close the app")
        os.system(f"{NPE}")

        os.system("sfc /scannow")
        print("SYSTEM FILE SCANNER scan completed.")
        os.system("dism /online /cleanup-image /restorehealth")
        print("DISM scan completed.")

        print("All scans completed.")
        print("cleaning files")
        os.system(n)
        os.system(l)
        input("click enter to restart pc")
        os.system("shutdown /r /t 0")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to complete one or more scans.")

download_anti()
run_antivirus_scans()
