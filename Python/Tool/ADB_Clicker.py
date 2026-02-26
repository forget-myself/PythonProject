import subprocess
import time
import sys
import re

import shutil

def run_adb_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running command {command}: {e}")
        return None

def get_devices():
    output = run_adb_command("adb devices")
    devices = []
    if output:
        lines = output.split('\n')
        for line in lines[1:]:
            if '\tdevice' in line:
                devices.append(line.split('\t')[0])
    return devices

def get_screen_size(device_id):
    output = run_adb_command(f"adb -s {device_id} shell wm size")
    # Physical size: 1080x2400
    match = re.search(r"Physical size: (\d+)x(\d+)", output)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

def main():
    if not shutil.which('adb'):
        print("Error: 'adb' command not found. Please install Android Platform Tools and add 'adb' to your PATH.")
        return

    print("Checking ADB devices...")
    devices = get_devices()
    
    if not devices:
        print("No devices found. Please connect your phone via USB or ensure ADB is enabled.")
        return

    device_id = devices[0]
    if len(devices) > 1:
        print("Multiple devices found:")
        for i, dev in enumerate(devices):
            print(f"{i}: {dev}")
        try:
            idx = int(input("Select device index: "))
            device_id = devices[idx]
        except (ValueError, IndexError):
            print("Invalid selection, using first device.")
            device_id = devices[0]
    
    print(f"Using device: {device_id}")
    
    size = get_screen_size(device_id)
    if not size:
        print("Could not get screen size.")
        return
        
    width, height = size
    print(f"Screen size: {width}x{height}")
    
    # Calculate coordinates
    # "Vertical screen middle position" implies centering horizontally (X axis)
    # "From top to bottom is 0-1" implies Y axis
    
    x = width // 2
    
    # "Take 0.2-0.8 area"
    y_start = int(height * 0.2)
    y_end = int(height * 0.8)
    
    step = 10
    interval = 0.05  # Short interval between clicks
    
    print(f"Clicking from Y={y_start} to Y={y_end} at X={x} with step {step}...")
    print("Press Ctrl+C to stop if needed.")
    print("Starting in 3 seconds... Switch to the target app now!")
    time.sleep(3)
    
    current_y = y_start
    count = 0
    
    try:
        while current_y <= y_end:
            cmd = f"adb -s {device_id} shell input tap {x} {current_y}"
            subprocess.run(cmd, shell=True) # Run without capturing output for speed
            # print(f"Clicked at ({x}, {current_y})") # Comment out to reduce spam/lag
            current_y += step
            count += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped by user.")
        
    print(f"Finished. Total clicks: {count}")

if __name__ == "__main__":
    main()
