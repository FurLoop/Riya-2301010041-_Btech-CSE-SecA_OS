import subprocess

def detect_vm():
    output = subprocess.getoutput("systeminfo")

    if "Hyper-V" in output or "Virtual" in output or "VMware" in output or "VirtualBox" in output:
        print("System is likely running inside a Virtual Machine.")
    else:
        print("No virtualization signature detected.")

detect_vm()
