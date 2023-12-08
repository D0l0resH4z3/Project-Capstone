

import os
import subprocess
import time
import hashlib
from ctypes import windll

def get_drive_status():
   
    devices = []
    record_device_bit = windll.kernel32.GetLogicalDrives()

    for label in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if record_device_bit & 1:
            devices.append(label)
        record_device_bit >>= 1

    return devices

def detect_device():
    original = set('C')
    
    print('Detecting USB drives...')
    
    new_devices = set(get_drive_status())
    
    added_devices = new_devices - original

    if added_devices:
        print(f"USB drive detected: {added_devices.pop()}")
        return True

    return False

def check_file_integrity(file_path, expected_hash):
   
    if os.path.exists(file_path):
        print(f"File {file_path} found. Checking integrity...")
        file_hash = calculate_hash(file_path)
        print(f"Calculated hash: {file_hash}")
        if file_hash == expected_hash:
            print("Integrity check passed.")
            return True
        else:
            print(f"Integrity check failed for {file_path}. Aborting.")
            exit()
    else:
        print(f"File {file_path} not found. Aborting.")
        exit()
    

def calculate_hash(file_path):
   
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def run_program(program_path):
   
    print(f"Running program: {program_path}")
    
    
    cmd_command = f'cd /D {os.path.splitdrive(program_path)[0]} && python3 GUI.py'
    subprocess.Popen(['start', 'cmd', '/K', cmd_command], shell=True)
    
    exit()

expected_hash = ''#the calculated hash of GUI.py
program_filename = 'GUI.py'

while True:
    if detect_device():
       
        usb_drive_path = os.path.join('D:', program_filename) 

        print(f"Checking USB drive: {usb_drive_path}")
        
        if check_file_integrity(usb_drive_path, expected_hash):
           
            run_program(usb_drive_path)
            break

    
    time.sleep(1)

