#!/usr/bin/env python3
import subprocess

# Define the output filename
output_filename = 'screenshot.png'

# Define the command to capture a screenshot of a selected area interactively
screenshot_cmd = ['import', '-frame', output_filename]

# Execute the 'import' command to capture the screenshot interactively
subprocess.run(screenshot_cmd)

# Copy the captured screenshot to the clipboard using xclip
copy_to_clipboard_cmd = ['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', 'screenshot.png']
subprocess.run(copy_to_clipboard_cmd)
