import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import Image
from ReadandWriteXMLs import main
import os

class home:

    
    top = tkinter.Tk()
    top.title("RoR2 Lifetime Stats Tracker")
    top.minsize(500,410)
    top.maxsize(500,410)
    top.geometry("500x410+100+100")
    
    canvas = tkinter.Canvas(top, width = 503, height = 415)
   
    #canvas.pack()
    canvas.place(relx = -0.003, rely = -0.01)

    bg_image = tkinter.PhotoImage(file = "ror2_bg.gif")
    canvas.create_image(0, 0, image = bg_image, anchor = NW)
    stats_LF = None
    
    def addRun():

        if len(main.RoR2PrevRun) == 0:
            main.noFileFound()
        else:
            if main.checkSeedMatch() == True:
                
                home.top.update()
                x = home.top.winfo_x()
                y = home.top.winfo_y()

                fail_window = tkinter.Toplevel()
                fail_window.minsize(250, 50)
                fail_window.maxsize(250, 50)
                fail_window.geometry("%dx%d+%d+%d" % (250, 50, x +120, y +155))

                message = Message(fail_window, text = "Most recent run already recorded.", width = 200)
                message.pack()

                ok_button = Button(fail_window, text = "OK", width = 10, command = fail_window.destroy)
                ok_button.pack()


            else:
                main.writeToLifeTimeStats()
                
                home.top.update()
                x = home.top.winfo_x()
                y = home.top.winfo_y()

                confirm_window = tkinter.Toplevel()
                confirm_window.minsize(250, 50)
                confirm_window.maxsize(250, 50)
                confirm_window.geometry("%dx%d+%d+%d" % (250, 50, x +120, y +155))
                
                message = Message(confirm_window, text = "Success")
                message.pack()

                ok_button = Button(confirm_window, text = "OK", width = 10, command = confirm_window.destroy)
                ok_button.pack()

    def createStatsLabelFrame():
        home.stats_LF = tkinter.LabelFrame(home.top, text = "Lifetime Stats",  font = "RiskofRainSquare" , fg = 'white', bg ='#596f81')
        return home.stats_LF

    def createBackButton():
        home.back_btn_window = home.canvas.create_window(5, 8, window = home.back_btn, anchor = NW, width = 60, height = 30)
        return home.back_btn_window

    def back_action():
        home.stats_LF.destroy()
        home.canvas.delete(home.back_btn_window)

        home.add_Run_Button_window = home.canvas.create_window(250, 100, window = home.Run_Button, anchor = CENTER, width = 150, height = 50)
        home.add_View_Stats_window = home.canvas.create_window(250, 310, window = home.View_Stats, anchor = CENTER, width = 210, height = 50)

    def statsPage():
        home.canvas.delete(home.add_View_Stats_window)
        home.canvas.delete(home.add_Run_Button_window)

        home.createBackButton()

        home.stats_LF = home.createStatsLabelFrame()
        home.stats_LF.place(relx = 0.5, rely = 0.5, anchor = CENTER)
       

        total_games_text = Label(home.stats_LF, text = "Total Games Played:", anchor = W,  font = "RiskofRainSquare" , fg = 'white', bg ='#596f81')
        total_games_text.grid(row = 0, column = 0, sticky = W, padx = 3)

        total_Games_Get = Label(home.stats_LF, text = main.getTotalGamesPlayed(),  font = "RiskofRainSquare" , fg = '#596f81' ,bg = "white")
        total_Games_Get.grid(row = 0, column = 1, sticky = E, ipadx = 5)



        current_fav_text = Label(home.stats_LF, text = "Favorite Survivor:", anchor = W,  font = "RiskofRainSquare" , fg = 'white' , bg ='#596f81')
        current_fav_text.grid(row = 1, column = 0, sticky = W, padx = 3)

        current_fav_get = Label(home.stats_LF, text = main.getCurrentFavorite(),  font = "RiskofRainSquare" ,  fg = '#596f81' ,bg = "white")
        current_fav_get.grid(row = 1, column = 1, sticky = E, ipadx = 5)



        dmg_text = Label(home.stats_LF, text = "Total Damage Dealt:", anchor = W,  font = "RiskofRainSquare" , fg = 'white' , bg ='#596f81')
        dmg_text.grid(row = 2, column = 0, sticky= W, padx = 3)

        dmg_get = Label(home.stats_LF, text = main.getLifetimeDMGDealt(),  font = "RiskofRainSquare" ,  fg = '#596f81' ,bg = "white")
        dmg_get.grid(row = 2, column = 1, sticky = E, ipadx= 5)



        avg_stages_text = Label(home.stats_LF, text = "Average Stages Per Run:", anchor = W,  font = "RiskofRainSquare" , fg = 'white' , bg ='#596f81')
        avg_stages_text.grid(row = 3, column = 0, sticky = W, padx = 3)

        avg_stages_get = Label(home.stats_LF, text = main.getAvgStagesPerRun(),  font = "RiskofRainSquare" ,  fg = '#596f81' ,bg = "white")
        avg_stages_get.grid(row = 3, column = 1, sticky = E, ipadx= 5)



        kills_text = Label(home.stats_LF, text = "Total Kills:", anchor = W,  font = "RiskofRainSquare" , fg = 'white' , bg ='#596f81')
        kills_text.grid(row = 4, column = 0, sticky= W, padx = 3)

        kills_get = Label(home.stats_LF, text = main.getLifetimeKills(),  font = "RiskofRainSquare" ,  fg = '#596f81' ,bg = "white")
        kills_get.grid(row = 4, column = 1, sticky = E, ipadx = 5)



        total_stages_text = Label(home.stats_LF, text = "Total Stages Beaten:", anchor = W,  font = "RiskofRainSquare" , fg = 'white' , bg ='#596f81')
        total_stages_text.grid(row = 5, column = 0, sticky = W, padx = 3)

        total_stages_get = Label(home.stats_LF, text = main.getTotalStages(),  font = "RiskofRainSquare" ,  fg = '#596f81' ,bg = "white")
        total_stages_get.grid(row = 5, column = 1, sticky = E, ipadx = 5)


    back_btn = tkinter.Button(top, text = "Back",  width = 5, height = 3, command = back_action, font = "RiskofRainSquare", fg = 'white', bg = "#041e3a")
    Run_Button = tkinter.Button(top, text = "Add Last Run", command = addRun, width = 100, height = 50, font = "RiskofRainSquare", fg = 'white', bg = "#16b7d5")
    View_Stats = tkinter.Button(top, text = "View Lifetime Stats", command = statsPage,  width = 210, height = 50, font = "RiskofRainSquare", fg = 'white', bg = "#0c659b")
    quit_button = tkinter.Button(top, text = "Quit", command = top.quit,  width = 50, height = 30, font = "RiskofRainSquare", fg = 'white', bg = "#041e3a")

    back_btn_window = canvas.create_window(5, 8, anchor = NW, width = 60, height = 30)
    add_Run_Button_window = canvas.create_window(250, 100, window = Run_Button, anchor = CENTER, width = 150, height = 50)
    add_View_Stats_window = canvas.create_window(250, 310, window = View_Stats, anchor = CENTER, width = 210, height = 50)
    add_quit_button_window = canvas.create_window(498, 409, window = quit_button, anchor = SE, width = 50, height = 30)


main.findPrevRunFile()

home.top.mainloop()