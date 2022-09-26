import xml.etree.ElementTree as ET
import os.path
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import path


class main:
    Life_Totals_XML = ET.parse("LifetimeTotals.xml")
    Life_Totals_XML_root = Life_Totals_XML.getroot()
    
    RoR2PrevRun = Life_Totals_XML_root.find("prevRunFileLocation").text

    def noFileFound():
        find_XML_window = tkinter.Tk()
        find_XML_window.title("RoR2 Lifetime Stats Tracker")
        find_XML_window.maxsize(500,180)
        find_XML_window.minsize(500,180)
        find_XML_window.attributes('-topmost', 'true')

        def findFileWindow():
            find_XML_window.attributes('-topmost', 'false')
            root = tkinter.Tk()
            root.attributes('-topmost', 'true')
            root.withdraw()
            fileLocation = filedialog.askdirectory(parent = root, initialdir = "C:\\", title = "Please select the PreviousRun.xml file")
            
            if len(fileLocation) > 1:
                for _file in os.listdir(fileLocation):
                    if _file == "PreviousRun.xml":
                        main.RoR2PrevRun = fileLocation+"/PreviousRun.xml"
                        main.Life_Totals_XML_root.find("prevRunFileLocation").text = fileLocation+"/PreviousRun.xml"
                        main.Life_Totals_XML.write('LifetimeTotals.xml')
                        find_XML_window.destroy()
                        break
                else:
                    find_XML_window.destroy()
                    main.noFileFound()
            else:
                root.destroy()
                find_XML_window.destroy()
                main.noFileFound()

            
            

        message = Message(find_XML_window, width = 490, justify = CENTER, anchor = CENTER, text = 
        '''
        The PreviousRun.xml file with your run data could not be found. Please locate the directory containing the file.
       
        Wherever you installed the game, the path is:

        ...\\Steam\\steamapps\\common\\Risk of Rain 2\\Risk of Rain 2_Data\\RunReports\\
        ''')
        message.pack()
        locate_button = Button(find_XML_window, width = 6, height = 2, command = findFileWindow, text = "Locate")
        locate_button.pack()

    

    def findPrevRunFile():
        if path.exists("C:\Program Files (x86)\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml") == True:
            main.RoR2PrevRun = "C:\Program Files (x86)\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml"
            main.Life_Totals_XML_root.find("prevRunFileLocation").text = "C:\Program Files (x86)\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml"
            main.Life_Totals_XML.write('LifetimeTotals.xml')
        elif path.exists("C:\Program Files\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml") == True:
            main.RoR2PrevRun = "C:\Program Files\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml"
            main.Life_Totals_XML_root.find("prevRunFileLocation").text = "C:\Program Files (x86)\Steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\RunReports\PreviousRun.xml"
            main.Life_Totals_XML.write('LifetimeTotals.xml')        
        elif path.exists(main.RoR2PrevRun):
            pass
        else:
            main.noFileFound()

           

    def writeToLifeTimeStats():
       
       #parse XMLs and get root elements  
        Prev_Run_XML = ET.parse(main.RoR2PrevRun)
        Prev_Run_XML_root = Prev_Run_XML.getroot()

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()

        #add one to total games played
        for element in Life_Totals_XML_root.iter("Stats"):
            new_total = int(element.find("totalGamesPlayed").text) + 1
            element.find("totalGamesPlayed").text = str(new_total)

        #add previous run stage count to Lifetime Total stage count
        for element in Prev_Run_XML_root.iter("fields"):
            if element.find("highestStagesCompleted") is None:
                break
                
            else:
                prev_run_stage_total = int(element.find("highestStagesCompleted").text)
                
                new_total = prev_run_stage_total + int(Life_Totals_XML_root.find("totalStagesCompleted").text)
                Life_Totals_XML_root.find("totalStagesCompleted").text = str(new_total)
                
                break
                

        #add one death per run 
        for element in Life_Totals_XML_root.iter("Stats"):
            new_total = int(element.find("totalDeaths").text) + 1
            element.find("totalDeaths").text = str(new_total)


        #Find new avg stage reached per run
        for element in Life_Totals_XML_root.iter("Stats"):
            new_total = int(element.find("totalStagesCompleted").text) / int(element.find("totalDeaths").text)
            element.find("avgStagesPerRun").text = str(round(new_total, 1))


        #add kills to Lifetime kills
        for element in Prev_Run_XML_root.iter("fields"):
            if element.find("totalKills") is None:
                break
                
            else:
                prev_run_kill_total = int(element.find("totalKills").text)

                new_total = prev_run_kill_total + int(Life_Totals_XML_root.find("lifetimeKills").text)
                Life_Totals_XML_root.find("lifetimeKills").text = str(new_total)

                break
                

        #add damage to Lifetime damage dealt
        for element in Prev_Run_XML_root.iter("fields"):
            if element.find("totalDamageDealt") is None:
                break

            else:
                prev_run_dmg_total = int(element.find("totalDamageDealt").text)
                
                new_total = prev_run_dmg_total + int(Life_Totals_XML_root.find("lifetimeDamageDealt").text)
                Life_Totals_XML_root.find("lifetimeDamageDealt").text = str(new_total)

                break

        #   Survivor nicknames--------------
                # Commando: CommandoBody
                # Huntress: HuntressBody 
                # MUL-T: ToolbotBody 
                # Engindeer: EngiBody 
                # Artif: MageBody 
                # Mercenary: MercBody
                # REX: TreebotBody
                # Loader: LoaderBody
                # Acrid: CrocoBody
                # Captain: CaptainBody

        #Find last survivor played and add 1 to the survivor lifetime played count
        for element in Prev_Run_XML_root.iter("PlayerInfo"):
            last_survivor = str(element.find("bodyName").text)

            for survivor in Life_Totals_XML_root.find("survivorCounts"):         
                if survivor.get("nick") == last_survivor:
                    new_total = int(survivor.text) + 1
                    survivor.text = str(new_total)
            break

        #Check for most played (Favorite) survivor
        current_Fav = []
        for survivor in Life_Totals_XML_root.find("survivorCounts"):
                if not current_Fav:
                    current_Fav.append(survivor)
                    continue
                else:
                    for fav in tuple(current_Fav):                
                        if int(survivor.text) < int(fav.text):
                            continue
                        elif int(survivor.text) > int(fav.text):
                            current_Fav.clear()
                            current_Fav.append(survivor)
                            break
                        else:
                            current_Fav.append(survivor)
                            break

        # *****May need to adjust to list or something later******   
        #Write Favorite List to single string and set <currentFav> to value
        Favorite_Survivor_String = "" 
        for fav in current_Fav:
            Favorite_Survivor_String += fav.get("name") + ", "
        
        Favorite_Survivor_String = Favorite_Survivor_String[:-2]
        Life_Totals_XML_root.find("currentFav").text = Favorite_Survivor_String
                    


        #record seed of previous run                
        last_seed = Prev_Run_XML_root.find("seed").text
        Life_Totals_XML_root.find("lastSeed").text = last_seed            


        #overwrite Lifetime Totals XML
        Life_Totals_XML.write('LifetimeTotals.xml')

    def getTotalGamesPlayed():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()
        
        totalGamesPlayed = Life_Totals_XML_root.find("totalGamesPlayed").text

        return totalGamesPlayed

    def getCurrentFavorite():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()
        
        currentFav = Life_Totals_XML_root.find("currentFav").text
        
        return currentFav
    
    def getLifetimeDMGDealt():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()
        
        dmg = Life_Totals_XML_root.find("lifetimeDamageDealt").text

        return dmg
    
    def getAvgStagesPerRun():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()
        
        avgStages = Life_Totals_XML_root.find("avgStagesPerRun").text
        return avgStages

    def getLifetimeKills():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()
        
        kills = Life_Totals_XML_root.find("lifetimeKills").text
        return kills
    
    def getTotalStages():
        #re-parse XMLs to check for updates while program is live

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()

        stages = Life_Totals_XML_root.find("totalStagesCompleted").text
        return stages

    def checkSeedMatch():  
        #re-parse XMLs to check for updates while program is live
        Prev_Run_XML = ET.parse(main.RoR2PrevRun)
        Prev_Run_XML_root = Prev_Run_XML.getroot()

        Life_Totals_XML = ET.parse("LifetimeTotals.xml")
        Life_Totals_XML_root = Life_Totals_XML.getroot()


        PrevRunSeed = Prev_Run_XML_root.find("seed").text
        checkSeed = Life_Totals_XML_root.find("lastSeed").text

        if checkSeed == PrevRunSeed:  
            return True
        else:
            return False

