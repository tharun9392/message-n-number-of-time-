# N Times Message Sender

A Python automation script that sends repetitive messages using keyboard input simulation.

## Description

This script uses `pyautogui` to automatically type and send messages. It randomly selects from a predefined list of animal sounds/messages and sends them 200 times with a brief delay between each message.

## Features

- Automated message sending using keyboard simulation
- Random selection from a list of predefined messages
- 8-second initial delay before starting (allows time to switch to target window)
- Sends 200 messages with automatic Enter key presses

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

Install the required dependencies:

```bash
pip install pyautogui
```

## Usage

1. Run the script:
   ```bash
   python n_times_mes_sender.py
   ```

2. Switch to your target window/application within the first 8 seconds (the script waits 8 seconds before starting)

3. The script will automatically type and send 200 random messages

## Messages

The script randomly selects from these predefined messages:
- NANNA
- oyeeeeeeeeeeee
- cheee
- bujjiii kondaa
- corryyyyyyyyy
- oseyyy
- bujjiii nannaaa
- hieee
- nannnnnnaaaaaaa

## Customization

To modify the messages, edit the `animals` list in the script:

```python
animals=['your', 'custom', 'messages', 'here']
```

To change the number of messages sent, modify the range value:

```python
for i in range(NUMBER_HERE):  # Change 200 to your desired number
```

To change the initial delay, modify the sleep time:

```python
time.sleep(X)  # Change 8 to your desired seconds
```

## Notes

- This script simulates keyboard input, so focus on the target application window after starting the script
- Use responsibly and only in applications where you have permission to send automated messages
