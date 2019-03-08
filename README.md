# Silent Screenshot Taking
Take screenshot silently.

## Usage
1. Install dependencies for Python
```bash
python3 install -r requirements.txt
```

2. Run script
```bash
Usage: main.py [OPTIONS] SAVE_PATH

Options:
  --special-key TEXT  key to take screenshot
  --debug             Print debug messages
  --help              Show this message and exit.
```

## Tips

### Running on macOS

Recent versions of masOS restrict monitoring of the keyboard for security reasons. To passthrough this restriction, one of the following must be true:
  - The process must run as root.
  - Your application must be white listed under Enable access for assistive devices. Note that this might require that you package your application, since otherwise the entire Python installation must be white listed.
  
Please note that this does not apply to monitoring of the mouse or trackpad.
