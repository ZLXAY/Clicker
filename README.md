# AutoClicker

A lightweight Python auto clicker with customizable mouse buttons, keybinds, and click delay. Perfect for automating repetitive mouse tasks with a simple hotkey.

---

## Features

* Start/stop clicking with a single key.
* Supports any mouse button (`left`, `right`, `middle`).
* Customizable click delay.
* Stop program instantly with `ESC`.
* Simple, easy-to-read Python code.

---

## Installation

1. Make sure you have Python 3 installed.
2. Install dependencies:

```bash
pip install mouse keyboard
```

3. Clone the repository:

```bash
git clone https://github.com/your-username/AutoClicker.git
cd AutoClicker
```

---

## Usage

```python
import Clicker  # Or whatever your module is named

if __name__ == "__main__":
    clicker = Clicker.SetClicker(mouseButton='left', keyBind='g', delayClick=0.5)
    clicker.startClick()
```

* Press your defined `keyBind` to start/stop clicking (`g` by default).
* Press `ESC` to exit the program.

---

## Customization

You can adjust the clicker settings:

* `mouseButton`: `"left"`, `"right"`, or `"middle"`.
* `keyBind`: any keyboard key to toggle clicking.
* `delayClick`: time in seconds between clicks (float or int).

Example:

```python
clicker = Clicker.SetClicker(mouseButton='right', keyBind='f', delayClick=0.2)
clicker.startClick()
```

---

## Notes

* Works on Windows, Linux, and MacOS.
* Make sure to run the script with administrator privileges if needed for your OS.

---

## License

MIT License © 2025 Your Name
