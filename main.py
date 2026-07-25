import appClasses

if __name__ == "__main__":
    root = appClasses.ctk.CTk()
    app = appClasses.pingPongApp(root)
    app.resetAll(noMenu=True,noSave=True)
    root.mainloop()