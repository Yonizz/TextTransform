from pynput.keyboard import Key, Listener, Controller
import win32clipboard, time, TTModules  #import of clipboard of the pc, the time and TTModules

keyboard = Controller()
COMBINAISONS = [[{Key.ctrl_l, Key.f1}, TTModules.swapcase]]
activation = False

currentPressed = set()      #represents the key that are in Combinaison AND that are pressed

def kCopyText(keyboard):
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl_l)

def kPasteText(keyboard):
    keyboard.press(Key.ctrl_l)   #push the key control on the left
    keyboard.press('v')          #push the key v
    keyboard.release('v')        #realease the key v
    keyboard.release(Key.ctrl_l) #realease the key control on the left

def GetClipboardData():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    TransformText(data)
    win32clipboard.CloseClipboard()
    return data

def TransformText(data, transform):
    global COMBINAISONS
    return COMBINAISONS[transform][1](data)

def UpdateClipboard(transform):
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    data = TransformText(data, transform)
    win32clipboard.SetClipboardText(data, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def on_press(key):
    global activation, transform
    if key in [keys for combinaison in COMBINAISONS for keys in combinaison[0]]:

        currentPressed.add(key)     #if the key is in the combinaison, we update the set Keys

        for i in range(0,len(COMBINAISONS)):
            if all(k in currentPressed for k in COMBINAISONS[i][0]):
                activation = True       #if every key is pressed, we launch the action on release
                transform = i

    if key == Key.esc:
        print("You ve stopped the listener")
        listener.stop()

def on_release(key):
    global activation, transform

    try:
        currentPressed.remove(key)  #if the current released key is in the combinaison, it is removed of the set, because it's released
        if len(currentPressed) == 0 and activation:     #if every key of the combinaison have been pressed (activation) and released (len() == 0)
            kCopyText(keyboard)
            time.sleep(0.2)
            UpdateClipboard(transform)
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
