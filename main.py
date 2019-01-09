from pynput.keyboard import Key, Listener, Controller
import win32clipboard, time

keyboard = Controller()
COMBINAISON = {Key.ctrl_l, Key.f1}
activation = False

currentPressed = set()      #represents the key that are in Combinaison AND that are pressed

def kCopyText(keyboard):
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl_l)

def kPasteText(keyboard):
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl_l)

def GetClipboardData():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    TransformText(data)
    win32clipboard.CloseClipboard()
    return data

def TransformText(data):
    return data.upper()

def UpdateClipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    data = TransformText(data)
    win32clipboard.SetClipboardText(data, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def on_press(key):
    global activation

    if key in COMBINAISON:
        currentPressed.add(key)     #if the key is in the combinaison, we update the setKey all(k in currentPressed for k in COMBINAISON):
        if all(k in currentPressed for k in COMBINAISON):
            activation = True       #if every key is pressed, we launch the action on release

    if key == Key.esc:
        print("You ve stopped the listener")
        listener.stop()

def on_release(key):
    global activation

    try:
        currentPressed.remove(key)  #if the current released key is in the combinaison, it is removed of the set, because it's released
        if len(currentPressed) == 0 and activation:     #if every key of the combinaison have been pressed (activation) and released (len() == 0)
            kCopyText(keyboard)
            time.sleep(0.2)
            UpdateClipboard()
            time.sleep(0.2)
            kPasteText(keyboard)
            time.sleep(0.2)
            activation = False                          #prevents from auto re-actvation

    except KeyError:
        pass


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
