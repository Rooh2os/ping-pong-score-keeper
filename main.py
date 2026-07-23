import appClass

if __name__ == "__main__":
    root = appClass.ctk.CTk()
    app = appClass.pingPongApp(root)
    app.resetAll(event="firstStart")
    root.mainloop()