import mouse
import keyboard
import time


class SetClicker:
    def __init__(self, mouseButton: str = 'left', keyBind: str = 'g', delayClick: int = 1 ) -> None:
        # Mouse button to be clicked ('left', 'right', etc.)
        self.mouseButton = mouseButton
        # Key to start/stop the auto clicker
        self.keyBind = keyBind
        # Delay between clicks (in seconds)
        self.delayClick = delayClick
        # Current clicker state (True = active, False = stopped)
        self.stateWork = False
        # Main flag to control the whole program
        self.workedClicker = True
        
        
    def changeState(self) -> None:
        # Toggle clicker state (start/stop)
        self.stateWork = not self.stateWork 
        # Print current state to console
        print(f"Clicker {'started' if self.stateWork else 'stop'}")
        
    def stopClicker(self):
        # Set flag to stop the main while loop
        self.workedClicker = False
        # Notify user that the program is shutting down
        print("Clicker turn-off")
        
    
    def startClick(self):
        
        # Hotkey to toggle clicker on/off
        keyboard.add_hotkey(f"{self.keyBind}", self.changeState)
        # Hotkey to completely stop the program
        keyboard.add_hotkey('esc', self.stopClicker)
        
        # Main clicking loop
        while self.workedClicker:
            
            if self.stateWork:
                # Perform mouse click with chosen button
                mouse.click(f"{self.mouseButton}")
                # Wait for defined delay before next click
                time.sleep(self.delayClick)
            
    
        