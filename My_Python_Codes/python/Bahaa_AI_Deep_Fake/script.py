# #@markdown # Step 1 (6 Minutes)

# from IPython.display import clear_output
# import torch
# import codecs

# if torch.cuda.is_available():
#   !apt-get update
#   !apt-get install -y nvidia-cuda-toolkit
#   device="cuda"
#   print("Using GPU")
# else:
#   device="cpu"
#   print("Using CPU")


# git_repo_rot13 = 'uggcf://tvguho.pbz/fcyraqbezntvp/ss_onunnnv'
# git_repo = codecs.decode(git_repo_rot13, 'rot 13')

# !git clone $git_repo --single-branch

# directory_rot13 = 'ss_onunnnv'
# directory = codecs.decode(directory_rot13, 'rot 13')

# %cd /content/$directory
# !python install.py --onnxruntime cuda-12.2 --skip-conda

# clear_output()
# print("Installed!")





















# #@markdown # Option 2 : Running On Local
# #@markdown _See how to Use this option down below_

# !npm install -g localtunnel
# !pip install colorama

# import subprocess
# import threading
# import time
# import socket
# import urllib.request

# def iframe_thread(port):
#     while True:
#         time.sleep(0.5)
#         sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = sock.connect_ex(('127.0.0.1', port))
#         if result == 0:
#             break
#         sock.close()

#         from colorama import Fore, Style
#     print (Fore.GREEN + "\nIP: ", Fore. RED, urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"), "\n", Style. RESET_ALL)
#     p = subprocess.Popen(["lt", "--port", "{}".format(port)], stdout=subprocess.PIPE)
#     for line in p.stdout:
#         print(line.decode(), end='')
# threading.Thread (target=iframe_thread, daemon=True, args=(7860,)).start()


# !python run.py














import torch
import codecs
import subprocess
import threading
import time
import socket
import urllib.request
import os
import subprocess

# Check for GPU availability and set device
if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")



# Decode and clone the GitHub repository
git_repo_rot13 = 'uggcf://tvguho.pbz/fcyraqbezntvp/ss_onunnnv'
git_repo = codecs.decode(git_repo_rot13, 'rot 13')

# Clone the repository
subprocess.run(['git', 'clone', git_repo, '--single-branch'])

# Change directory to the cloned repo using os.chdir()
directory_rot13 = 'ss_onunnnv'
directory = codecs.decode(directory_rot13, 'rot 13')

# Change the current working directory to the cloned repository
os.chdir(directory)

# Install dependencies locally
subprocess.run(['python', 'install.py', '--onnxruntime', 'cuda-12.2', '--skip-conda'])


print("Installed!")

# Installing localtunnel and colorama
subprocess.run(['npm', 'install', '-g', 'localtunnel'])
subprocess.run(['pip', 'install', 'colorama'])

# Function to check if the server is running
def iframe_thread(port):
    while True:
        time.sleep(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            break
        sock.close()

    # Get public IP and run localtunnel
    public_ip = urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n")
    print(f"IP: {public_ip}")
    subprocess.Popen(["lt", "--port", f"{port}"], stdout=subprocess.PIPE)

# Start a thread to run the iframe function
threading.Thread(target=iframe_thread, daemon=True, args=(7860,)).start()

# Finally, run the Python script
subprocess.run(['python', 'run.py'])
