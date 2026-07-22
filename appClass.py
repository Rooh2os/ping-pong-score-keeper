import customtkinter as ctk
import pyglet
import tkinter as tk
from tkinter import messagebox
from PIL import Image

pyglet.options['win32_gdi_font'] = True
pyglet.resource.add_font('assets/Nunito.ttf')  

class pingPongApp:
    def resetAll(self,event=None):
        self.scoreReset()
        self.nameReset()
    
    def scoreReset(self,event=None):
        self.playerAScore = 0
        self.playerBScore = 0

        self.playerAScoreVar.set(str(self.playerAScore))
        self.playerBScoreVar.set(str(self.playerBScore))

    def nameReset(self,event=None):
        self.playerANameVar.set("Player A")
        self.playerBNameVar.set("Player B")

        self.playerANameChange()
        self.playerBNameChange()



    def scoreIncreasePlayerA(self,event=None):
        self.playerAScore += 1
        self.playerAScoreVar.set(str(self.playerAScore))
        self.serveSwitch()
        
    def scoreIncreasePlayerB(self,event=None):
        self.playerBScore += 1
        self.playerBScoreVar.set(str(self.playerBScore))
        self.serveSwitch()

    def scoreDecreasePlayerA(self,event=None):
        if self.playerAScore > 0:
            self.playerAScore -= 1
            self.playerAScoreVar.set(str(self.playerAScore))
        
    def scoreDecreasePlayerB(self,event=None):
        if self.playerBScore > 0:
            self.playerBScore -= 1
            self.playerBScoreVar.set(str(self.playerBScore))
    
    def playerAScoreChange(self, event=None):
        dialog = ctk.CTkInputDialog(
            text="Enter new score for Player A:",
            title="Change Score",
            fg_color="#595959",
            text_color="white",
            font=("Nunito", 30)
        )
        
        newScore = dialog.get_input()
        
        if newScore:
            try:
                formattedScore = int(newScore.strip())
                
                if formattedScore >= 0:
                    self.playerAScore = formattedScore
                    self.playerAScoreVar.set(str(formattedScore))
                else:
                    # 🟡 Warning popup for negative numbers
                    messagebox.showwarning("Invalid Score", "Score cannot be negative!")

            except ValueError:
                # 🔴 Error popup if they type letters or symbols
                messagebox.showerror("Invalid Input", "Please enter a valid whole number!")

    def playerBScoreChange(self, event=None):
        dialog = ctk.CTkInputDialog(
            text="Enter new score for Player B:",
            title="Change Score",
            fg_color="#595959",
            text_color="white",
            font=("Nunito", 30)
        )
        
        newScore = dialog.get_input()
        
        if newScore:
            try:
                formattedScore = int(newScore.strip())
                
                if formattedScore >= 0:
                    self.playerBScore = formattedScore
                    self.playerBScoreVar.set(str(formattedScore))
                else:
                    # 🟡 Warning popup for negative numbers
                    messagebox.showwarning("Invalid Score", "Score cannot be negative!")

            except ValueError:
                # 🔴 Error popup if they type letters or symbols
                messagebox.showerror("Invalid Input", "Please enter a valid whole number!")


    def playerANameChange(self,event=None):
        # 1. Create and display the popup dialog
        dialog = ctk.CTkInputDialog(text="Enter new name for Player A:",
                                    title="Change Name",
                                    fg_color="#595959",
                                    text_color="white",
                                    font=("Nunito", 30)
                                    )
        
        # 2. Get the input (this pauses and waits for the user to click OK/Cancel)
        newName = dialog.get_input()
        
        # 3. If they typed a name and didn't press Cancel, update the label!
        if newName:
            # .strip() removes accidental extra spaces at the beginning or end
            # .title() capitalizes the first letter of every word
            formattedName = newName.strip().title()
            
            # Make sure they didn't just type empty spaces
            if formattedName:
                self.playerANameVar.set(formattedName)

    def playerBNameChange(self,event=None):
        # 1. Create and display the popup dialog
        dialog = ctk.CTkInputDialog(text="Enter new name for Player B:",
                                    title="Change Name",
                                    fg_color="#595959",
                                    text_color="white",
                                    font=("Nunito", 30)
                                    )
        
        # 2. Get the input (this pauses and waits for the user to click OK/Cancel)
        newName = dialog.get_input()
        
        # 3. If they typed a name and didn't press Cancel, update the label!
        if newName:
            # .strip() removes accidental extra spaces at the beginning or end
            # .title() capitalizes the first letter of every word
            formattedName = newName.strip().title()
            
            # Make sure they didn't just type empty spaces
            if formattedName:
                self.playerBNameVar.set(formattedName)


    def serveSwitch(self,event=None):
        if self.serveCount < 3:
            self.serveCount += 1
        else:
            self.serveCount = 0
        #print(self.serveCount)
        if self.serveCount < 2:
            self.serveBLabel.configure(image=self.texture_noServe)
            if self.serveCount == 0:
                self.serveALabel.configure(image=self.texture_firstServe)
            else:
                self.serveALabel.configure(image=self.texture_secondServe)
        else:
            self.serveALabel.configure(image=self.texture_noServe)
            if self.serveCount == 2:
                self.serveBLabel.configure(image=self.texture_firstServe)
            else:
                self.serveBLabel.configure(image=self.texture_secondServe)

    def pPass(self,event=None):
        print("passed")
    
    def __init__(self,root):

        self.root = root
        
        #self.root = ctk.CTk() #make sure to comment before running

        
        self.root.title("Ping pong score keeper")
        self.root.geometry("960x540")
        self.root.minsize(300,150)
        self.root.configure(fg_color="#595959")


        # Setup rows and columns for .grid (y-x)/a*10000 to give greater accuracy
        for row in range(4):
            self.root.rowconfigure(row, weight=(1592,1444,1037,5925)[row], minsize=1)

        for column in range(5):
            self.root.columnconfigure(column, weight=(3500,979,1041,979,3500)[column], minsize=1)

        #Make string vars

        self.playerAScoreVar = ctk.StringVar(value="0")

        self.playerBScoreVar = ctk.StringVar(value="0")

        self.playerANameVar = ctk.StringVar(value="Player A")

        self.playerBNameVar = ctk.StringVar(value="Player B")

        self.serveCount = 0 #0 = first serve, player A; 1 = second serve, player A; 2 = first serve, player B; 3 = second serve, player B


        # 1. Create the master menu bar object
        self.menuBar = tk.Menu(self.root,
                          font=("Nunito", 11),
                          bg="#595959",
                          fg="white",
                          activebackground="#579d95", # Teal hover highlight
                          activeforeground="white",
                          )
        self.root.config(menu=self.menuBar) # Tell the window to use this menu bar

        # 2. Create the "File" dropdown menu
        # 'tearoff=0' stops the user from detaching the menu into a separate floating window
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0,font=("Nunito", 11),
                          bg="#595959",
                          fg="white",
                          activebackground="#579d95", # Teal hover highlight
                          activeforeground="white",)

        # 3. Add actual options inside the "File" menu
        self.fileMenu.add_command(label="New Game", command=self.resetAll, accelerator="Ctrl+N")
        self.fileMenu.add_command(label="New Match", command=self.scoreReset, accelerator="Ctrl+M")
        self.fileMenu.add_separator() # Adds a nice divider line
        self.fileMenu.add_command(label="Exit", command=self.root.quit)

        # 4. Cascade (attach) the "File" dropdown to the master menu bar
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        #Make the edit menu
        self.editMenu = tk.Menu(self.menuBar,tearoff=0,font=("Nunito", 11),
                          bg="#595959",
                          fg="white",
                          activebackground="#579d95", # Teal hover highlight
                          activeforeground="white",)
        
        self.editMenu_scoreMenu = tk.Menu(self.editMenu,tearoff=0,font=("Nunito", 11),
                          bg="#595959",
                          fg="white",
                          activebackground="#579d95", # Teal hover highlight
                          activeforeground="white",)
        self.editMenu_scoreMenu.add_command(label="Player A", command=self.playerAScoreChange)
        self.editMenu_scoreMenu.add_command(label="Player B", command=self.playerBScoreChange)
        self.editMenu_scoreMenu.add_separator()
        self.editMenu_scoreMenu.add_command(label="Reset Score", command=self.scoreReset)
        
        
        
        self.editMenu_renameMenu = tk.Menu(self.editMenu,tearoff=0,font=("Nunito", 11),
                          bg="#595959",
                          fg="white",
                          activebackground="#579d95", # Teal hover highlight
                          activeforeground="white",)
        
        self.editMenu_renameMenu.add_command(label="Player A", command=self.playerANameChange)
        self.editMenu_renameMenu.add_command(label="Player B", command=self.playerBNameChange)
        self.editMenu_renameMenu.add_separator()
        self.editMenu_renameMenu.add_command(label="Reset Names", command=self.nameReset)

        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

        self.editMenu.add_cascade(label="Change Score:", menu=self.editMenu_scoreMenu)
        self.editMenu.add_separator()
        self.editMenu.add_cascade(label="Rename Player:", menu=self.editMenu_renameMenu)
        

        #Make the right button for player B
        self.rightButton = ctk.CTkButton(self.root, 
                                     text="▶", font=("Nunito", 50 , "bold"), 
                                     fg_color="#579d95", 
                                     hover_color="#477b75",
                                     text_color="white", 
                                     corner_radius=90,
                                     command=self.scoreIncreasePlayerB
                                     )
        self.rightButton.grid(row=3,
                              column=4,
                              sticky="nsew",
                              )

        #Make the left button for player A
        self.leftButton = ctk.CTkButton(self.root, 
                                    text="◀", font=("Nunito", 50 , "bold"), 
                                    fg_color="#579d95", 
                                     hover_color="#477b75",
                                     text_color="white", 
                                     corner_radius=90,
                                    command=self.scoreIncreasePlayerA
                                    )
        self.leftButton.grid(row=3,
                              column=0,
                              sticky="nsew",
                            )
        

        #Make the down button for player B
        self.rightDownButton = ctk.CTkButton(self.root, 
                                     text="▼", font=("Nunito", 50 , "bold"), 
                                     fg_color="#9d5757", 
                                     hover_color="#6e3c3c",
                                     text_color="white", 
                                     corner_radius=90,
                                     command=self.scoreDecreasePlayerB
                                     )
        self.rightDownButton.grid(row=3,
                              column=3,
                              sticky="nsew"
                              )

        #Make the down button for player A
        self.leftDownButton = ctk.CTkButton(self.root, 
                                     text="▼", font=("Nunito", 50 , "bold"), 
                                     fg_color="#9d5757", 
                                     hover_color="#6e3c3c",
                                     text_color="white", 
                                     corner_radius=90,
                                     command=self.scoreDecreasePlayerA
                                     )
        self.leftDownButton.grid(row=3,
                              column=1,
                              sticky="nsew"
                              )    
        
        #Make the serve switch button
        self.serveSwitchButton = ctk.CTkButton(self.root, 
                                     text="⇄", font=("Nunito", 50 , "bold"),
                                     hover_color="#3f4c6f", 
                                     fg_color="#576a9d", 
                                     text_color="white", 
                                     corner_radius=90,
                                     command=self.serveSwitch,
                                     )
        self.serveSwitchButton.grid(row=1,
                              column=2,
                              sticky="nsew"
                              )

        #Make the serve indicators
        image_firstServe = Image.open("assets/firstServe.png")
        image_secondServe = Image.open("assets/secondServe.png")
        image_noServe = Image.open("assets/noServe.png")

        self.texture_firstServe = ctk.CTkImage(light_image=image_firstServe, dark_image=image_firstServe, size=(150,150))
        self.texture_secondServe = ctk.CTkImage(light_image=image_secondServe, dark_image=image_secondServe, size=(150,150))
        self.texture_noServe = ctk.CTkImage(light_image=image_noServe, dark_image=image_noServe, size=(150,150))

        self.serveALabel = ctk.CTkLabel(self.root, text="", image=self.texture_firstServe)
        self.serveALabel.grid(row=1, column=1, sticky="nsew")

        self.serveBLabel = ctk.CTkLabel(self.root, text="", image=self.texture_noServe)
        self.serveBLabel.grid(row=1, column=3, sticky="nsew")



        #Make bind for player A
        self.root.bind("<Left>", self.scoreIncreasePlayerA)

        #Make bind for player B
        self.root.bind("<Right>", self.scoreIncreasePlayerB)

        #Make bind for new match and new game
        self.root.bind("<Control-m>", self.scoreReset)
        self.root.bind("<Control-n>", self.resetAll)

        
        #Make the name label for player A
        self.playerANameLabel = ctk.CTkLabel(
            self.root, 
            textvariable=self.playerANameVar, 
            font=("Nunito", 30, "bold"),
            text_color="white"
        )
        self.playerANameLabel.grid(row=2, column=0, sticky="nsew")
        self.playerANameLabel.bind("<Button-1>", self.playerANameChange)

        # Player A Score Label
        self.playerAScoreLabel = ctk.CTkLabel(
            self.root, 
            textvariable=self.playerAScoreVar, 
            font=("Nunito", 90, "bold"),
            text_color="white"
        )
        self.playerAScoreLabel.grid(row=1, column=0, sticky="nsew")

        #Make the name label for player B
        self.playerBNameLabel = ctk.CTkLabel(
            self.root, 
            textvariable=self.playerBNameVar, 
            font=("Nunito", 30, "bold"),
            text_color="white"
        )
        self.playerBNameLabel.grid(row=2, column=4, sticky="nsew")
        self.playerBNameLabel.bind("<Button-1>", self.playerBNameChange)

        # Player B Score Label
        self.playerBScoreLabel = ctk.CTkLabel(
            self.root, 
            textvariable=self.playerBScoreVar, 
            font=("Nunito", 90, "bold"),
            text_color="white"
        )
        self.playerBScoreLabel.grid(row=1, column=4, sticky="nsew")





if __name__ == "__main__":
    import sys
    import subprocess

    print("Redirecting to main script...")
    
    # Launch main.py and exit this script
    subprocess.run([sys.executable, "main.py"])