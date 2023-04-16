import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import filedialog
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
import os

root = tk.Tk()  # create tk.mainframe
root.withdraw()  # hide the mainframe from view
cur_dir = os.getcwd()  # acquire current directory
temp_dir = filedialog.askdirectory(  # set temp dir through file dialog
    parent=root, initialdir=cur_dir,
    title='Please select tes3mp folder directory')

true_string = " = true"
config_string = "config."
html_center_string = "<center><p style=\"color:white\">"
html_end_string = "</p></center>"
false_string = " = false"

config_dict = {"passTimeWhenEmpty =": '', "allowConsole =": '', "allowBedRest =": '', "allowWildernessRest =": '',
               "allowWait =": '', "shareJournal =": '', "shareFactionRanks =": '', "shareFactionExpulsion =": '',
               "shareFactionReputation =": '', "shareTopics =": '', "shareBounty =": '', "shareReputation =": '',
               "shareMapExploration =": '', "shareVideos =": '', "respawnAtImperialShrine =": '',
               "respawnAtTribunalTemple =": '', "playersRespawn =": '', "bountyResetOnDeath =": '',
               "bountyDeathPenalty =": '', "allowSuicideCommand =": '', "allowFixmeCommand =": '',
               "enablePlayerCollision =": '', "enforceDataFiles =": '', "loginTime =": '', "difficulty =": '',
               "deathTime =": '', "deathPenaltyJailDays =": ''}  # dictionary for config.lua

server_dict = {"port =": '', "enabled =": '', "hostname =": '', "maximumPlayers =": '', "password =": '',
               "localAddress =": ''}  # dictionary for tes3mp-server-default.cfg


def fetch_files():
    global config_content
    global server_content
    global server_config_dir
    global config_dir
    config_dir = os.path.join(temp_dir, './', "server", './', "scripts", './' + 'config.lua')  # set path to cfg file
    config_file = open(config_dir, "r+")  # open configuration with read/write permission
    config_content = config_file.readlines()  # read file to a variable
    config_file.close()  # close file
    server_config_dir = os.path.join(temp_dir, './' + 'tes3mp-server-default.cfg')  # set path to server config file
    server_file = open(server_config_dir, "r+")  # open configuration with read/write permission
    server_content = server_file.readlines()  # read file to a variable
    server_file.close()  # close file

    for key in server_dict:  # iterate through keys in dictionary
        for line in server_content:  # go through lines in config file content
            if key in line:  # search for the phrase
                if str(key) == "port =":  # there are two param. with this name, only one is important
                    for line_number, nr_line in enumerate(server_content, 1):  # number lines
                        if key in nr_line:  # if the key exist in line
                            x = line.rfind("=")  # find desired character
                            x = x + 2  # increment = position by 2
                            value = line[x:]  # read content after this position
                            value = value.strip()  # strip of unwanted characters
                            server_dict[key] = value  # assign it to dictionary
                            break  # finish after the first parameter was assigned
                    break  # break the loop after the first parameter was assigned
                else:
                    x = line.rfind("=")  # find desired character
                    x = x + 2  # increment = position by 2
                    value = line[x:]  # read content after this position
                    value = value.strip()  # strip of unwanted characters
                    if str(value) == "false":  # check value
                        server_dict[key] = str(value)  # assign value to dictionary
                    elif str(value) == "true":  # check value
                        server_dict[key] = str(value)  # assign value to dictionary
                    else:  # if value is different from true and false
                        server_dict[key] = value  # assign it to dictionary


def reload():
    fetch_files()
    for key in config_dict:  # iterate through keys in dictionary
        for line in config_content:  # go through lines in config file content
            if key in line:  # search for the phrase
                x = line.rfind("=")  # find desired character
                x = x + 2  # increment = position by 2
                value = line[x:]  # read content after this position
                value = value.strip()  # strip of unwanted characters
                if str(value) == "false":  # check value
                    config_dict[key] = str(value)  # assign value to dictionary
                elif str(value) == "true":  # check value
                    config_dict[key] = str(value)  # assign value to dictionary
                else:  # if value is different from true and false
                    config_dict[key] = value  # assign it to dictionary


class Ui(QtWidgets.QMainWindow):  # class for GUI

    def __init__(self):  # initialise GUI function
        super().__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self)  # Load the .ui file

        reload()

        self.passTimeWhenEmpty = self.findChild(QtWidgets.QCheckBox, 'passTimeWhenEmpty')  # Find the checkbox
        if str(config_dict["passTimeWhenEmpty ="]) == "true":  # Read value
            self.passTimeWhenEmpty.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["passTimeWhenEmpty ="]) == "false":  # Read value
            self.passTimeWhenEmpty.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.passTimeWhenEmpty.stateChanged.connect(self.boolean_config_change)  # call function

        self.allowConsole = self.findChild(QtWidgets.QCheckBox, 'allowConsole')  # Find the checkbox
        if str(config_dict["allowConsole ="]) == "true":  # Read value
            self.allowConsole.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowConsole ="]) == "false":  # Read value
            self.allowConsole.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowConsole.stateChanged.connect(self.boolean_config_change)  # call function

        self.allowBedRest = self.findChild(QtWidgets.QCheckBox, 'allowBedRest')  # Find the checkbox
        if str(config_dict["allowBedRest ="]) == "true":  # Read value
            self.allowBedRest.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowBedRest ="]) == "false":  # Read value
            self.allowBedRest.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowBedRest.stateChanged.connect(self.boolean_config_change)  # call function

        self.allowWildernessRest = self.findChild(QtWidgets.QCheckBox, 'allowWildernessRest')  # Find the checkbox
        if str(config_dict["allowWildernessRest ="]) == "true":  # Read value
            self.allowWildernessRest.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowWildernessRest ="]) == "false":  # Read value
            self.allowWildernessRest.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowWildernessRest.stateChanged.connect(self.boolean_config_change)  # call method

        self.allowWait = self.findChild(QtWidgets.QCheckBox, 'allowWait')  # Find the function
        if str(config_dict["allowWait ="]) == "true":  # Read value
            self.allowWait.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowWait ="]) == "false":  # Read value
            self.allowWait.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowWait.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareJournal = self.findChild(QtWidgets.QCheckBox, 'shareJournal')  # Find the checkbox
        if str(config_dict["shareJournal ="]) == "true":  # Read value
            self.shareJournal.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareJournal ="]) == "false":  # Read value
            self.shareJournal.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareJournal.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareFactionRanks = self.findChild(QtWidgets.QCheckBox, 'shareFactionRanks')  # Find the checkbox
        if str(config_dict["shareFactionRanks ="]) == "true":  # Read value
            self.shareFactionRanks.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareFactionRanks ="]) == "false":  # Read value
            self.shareFactionRanks.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareFactionRanks.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareFactionExpulsion = self.findChild(QtWidgets.QCheckBox, 'shareFactionExpulsion')  # Find the checkbox
        if str(config_dict["shareFactionExpulsion ="]) == "true":  # Read value
            self.shareFactionExpulsion.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareFactionExpulsion ="]) == "false":  # Read value
            self.shareFactionExpulsion.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareFactionExpulsion.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareFactionReputation = self.findChild(QtWidgets.QCheckBox, 'shareFactionReputation')  # Find the checkbox
        if str(config_dict["shareFactionReputation ="]) == "true":  # Read value
            self.shareFactionReputation.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareFactionReputation ="]) == "false":  # Read value
            self.shareFactionReputation.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareFactionReputation.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareTopics = self.findChild(QtWidgets.QCheckBox, 'shareTopics')  # Find the checkbox
        if str(config_dict["shareTopics ="]) == "true":  # Read value
            self.shareTopics.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareTopics ="]) == "false":  # Read value
            self.shareTopics.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareTopics.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareBounty = self.findChild(QtWidgets.QCheckBox, 'shareBounty')  # Find the checkbox
        if str(config_dict["shareBounty ="]) == "true":  # Read value
            self.shareBounty.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareBounty ="]) == "false":  # Read value
            self.shareBounty.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareBounty.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareReputation = self.findChild(QtWidgets.QCheckBox, 'shareReputation')  # Find the checkbox
        if str(config_dict["shareReputation ="]) == "true":  # Read value
            self.shareReputation.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareReputation ="]) == "false":  # Read value
            self.shareReputation.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareReputation.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareMapExploration = self.findChild(QtWidgets.QCheckBox, 'shareMapExploration')  # Find the checkbox
        if str(config_dict["shareMapExploration ="]) == "true":  # Read value
            self.shareMapExploration.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareMapExploration ="]) == "false":  # Read value
            self.shareMapExploration.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareMapExploration.stateChanged.connect(self.boolean_config_change)  # call function

        self.shareVideos = self.findChild(QtWidgets.QCheckBox, 'shareVideos')  # Find the checkbox
        if str(config_dict["shareVideos ="]) == "true":  # Read value
            self.shareVideos.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["shareVideos ="]) == "false":  # Read value
            self.shareVideos.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.shareVideos.stateChanged.connect(self.boolean_config_change)  # call method

        self.respawnAtImperialShrine = self.findChild(QtWidgets.QCheckBox, 'respawnAtImperialShrine')  # Find the ch.box
        if str(config_dict["respawnAtImperialShrine ="]) == "true":  # Read value
            self.respawnAtImperialShrine.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["respawnAtImperialShrine ="]) == "false":  # Read value
            self.respawnAtImperialShrine.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.respawnAtImperialShrine.stateChanged.connect(self.boolean_config_change)  # call function

        self.respawnAtTribunalTemple = self.findChild(QtWidgets.QCheckBox, 'respawnAtTribunalTemple')  # Find the ch.box
        if str(config_dict["respawnAtTribunalTemple ="]) == "true":  # Read value
            self.respawnAtTribunalTemple.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["respawnAtTribunalTemple ="]) == "false":  # Read value
            self.respawnAtTribunalTemple.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.respawnAtTribunalTemple.stateChanged.connect(self.boolean_config_change)  # call function

        self.playersRespawn = self.findChild(QtWidgets.QCheckBox, 'playersRespawn')  # Find the checkbox
        if str(config_dict["playersRespawn ="]) == "true":  # Read value
            self.playersRespawn.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["playersRespawn ="]) == "false":  # Read value
            self.playersRespawn.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.playersRespawn.stateChanged.connect(self.boolean_config_change)  # call function

        self.bountyResetOnDeath = self.findChild(QtWidgets.QCheckBox, 'bountyResetOnDeath')  # Find the checkbox
        if str(config_dict["bountyResetOnDeath ="]) == "true":  # Read value
            self.bountyResetOnDeath.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["bountyResetOnDeath ="]) == "false":  # Read value
            self.bountyResetOnDeath.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.bountyResetOnDeath.stateChanged.connect(self.boolean_config_change)  # call function

        self.bountyDeathPenalty = self.findChild(QtWidgets.QCheckBox, 'bountyDeathPenalty')  # Find the checkbox
        if str(config_dict["bountyDeathPenalty ="]) == "true":  # Read value
            self.bountyDeathPenalty.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["bountyDeathPenalty ="]) == "false":  # Read value
            self.bountyDeathPenalty.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.bountyDeathPenalty.stateChanged.connect(self.boolean_config_change)  # call function

        self.allowSuicideCommand = self.findChild(QtWidgets.QCheckBox, 'allowSuicideCommand')  # Find the checkbox
        if str(config_dict["allowSuicideCommand ="]) == "true":  # Read value
            self.allowSuicideCommand.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowSuicideCommand ="]) == "false":  # Read value
            self.allowSuicideCommand.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowSuicideCommand.stateChanged.connect(self.boolean_config_change)  # call function

        self.allowFixmeCommand = self.findChild(QtWidgets.QCheckBox, 'allowFixmeCommand')  # Find the checkbox
        if str(config_dict["allowFixmeCommand ="]) == "true":  # Read value
            self.allowFixmeCommand.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["allowFixmeCommand ="]) == "false":  # Read value
            self.allowFixmeCommand.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.allowFixmeCommand.stateChanged.connect(self.boolean_config_change)  # call function

        self.enablePlayerCollision = self.findChild(QtWidgets.QCheckBox, 'enablePlayerCollision')  # Find the checkbox
        if str(config_dict["enablePlayerCollision ="]) == "true":  # Read value
            self.enablePlayerCollision.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["enablePlayerCollision ="]) == "false":  # Read value
            self.enablePlayerCollision.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.enablePlayerCollision.stateChanged.connect(self.boolean_config_change)  # call function

        self.enforceDataFiles = self.findChild(QtWidgets.QCheckBox, 'enforceDataFiles')  # Find the checkbox
        if str(config_dict["enforceDataFiles ="]) == "true":  # Read value
            self.enforceDataFiles.setCheckState(Qt.CheckState.Checked)  # check box
        if str(config_dict["enforceDataFiles ="]) == "false":  # Read value
            self.enforceDataFiles.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.enforceDataFiles.stateChanged.connect(self.boolean_config_change)  # call function

        self.enabled = self.findChild(QtWidgets.QCheckBox, 'enabled')  # Find the checkbox
        if str(server_dict["enabled ="]) == "true":  # Read value
            self.enabled.setCheckState(Qt.CheckState.Checked)  # check box
        if str(server_dict["enabled ="]) == "false":  # Read value
            self.enabled.setCheckState(Qt.CheckState.Unchecked)  # uncheck box
        self.enabled.stateChanged.connect(self.boolean_server_config_change)  # call function

        self.loginTimeoutView = self.findChild(QtWidgets.QTextBrowser, 'loginTimeoutView')  # Find the text browser
        self.loginTimeoutView.setHtml(html_center_string + config_dict["loginTime ="] +
                                      html_end_string)  # Show the content of variable in html form
        self.loginTime = self.findChild(QtWidgets.QPushButton, 'loginTime')  # Find the button
        self.loginTime.clicked.connect(self.param_config_change)  # Connect button to a function

        self.difficultyView = self.findChild(QtWidgets.QTextBrowser, 'difficultyView')  # Find the text browser
        self.difficultyView.setHtml(html_center_string + config_dict["difficulty ="] +
                                    html_end_string)  # Show the content of variable in html form
        self.difficulty = self.findChild(QtWidgets.QPushButton, 'difficulty')  # Find the button
        self.difficulty.clicked.connect(self.param_config_change)  # Connect button to a function

        self.deathTimeView = self.findChild(QtWidgets.QTextBrowser, 'deathTimeView')  # Find the text browser
        self.deathTimeView.setHtml(html_center_string + config_dict["deathTime ="] +
                                   html_end_string)  # Show the content of variable in html form

        self.deathTime = self.findChild(QtWidgets.QPushButton, 'deathTime')  # Find the button
        self.deathTime.clicked.connect(self.param_config_change)  # Connect button to a function

        self.deathPenaltyJailDays = self.findChild(QtWidgets.QTextBrowser, 'deathPenaltyView')  # Find the text browser
        self.deathPenaltyView.setHtml(html_center_string + config_dict["deathPenaltyJailDays ="] +
                                      html_end_string)  # Show the content of variable in html form

        self.deathPenaltyJailDays = self.findChild(QtWidgets.QPushButton, 'deathPenaltyJailDays')  # Find the button
        self.deathPenaltyJailDays.clicked.connect(self.param_config_change)  # Connect button to a function

        self.portView = self.findChild(QtWidgets.QTextBrowser, 'portView')  # Find the text browser
        self.portView.setHtml(html_center_string + server_dict["port ="] +
                              html_end_string)  # Show the content of variable in html form

        self.port = self.findChild(QtWidgets.QPushButton, 'port')  # Find the button
        self.port.clicked.connect(self.param_server_config_change)  # Connect button to a function

        self.localAddressView = self.findChild(QtWidgets.QTextBrowser, 'localAddressView')  # Find the text browser
        self.localAddressView.setHtml(html_center_string + server_dict["localAddress ="] +
                                      html_end_string)  # Show the content of variable in html form

        self.localAddress = self.findChild(QtWidgets.QPushButton, 'localAddress')  # Find the button
        self.localAddress.clicked.connect(self.param_server_config_change)  # Connect button to a function

        self.hostnameView = self.findChild(QtWidgets.QTextBrowser, 'hostnameView')  # Find the text browser
        self.hostnameView.setHtml(html_center_string + server_dict["hostname ="] +
                                  html_end_string)  # Show the content of variable in html form

        self.hostname = self.findChild(QtWidgets.QPushButton, 'hostname')  # Find the button
        self.hostname.clicked.connect(self.param_server_config_change)  # Connect button to a function

        self.playersView = self.findChild(QtWidgets.QTextBrowser, 'playersView')  # Find the text browser
        self.playersView.setHtml(html_center_string + server_dict["maximumPlayers ="] +
                                 html_end_string)  # Show the content of variable in html form

        self.maximumPlayers = self.findChild(QtWidgets.QPushButton, 'maximumPlayers')  # Find the button
        self.maximumPlayers.clicked.connect(self.param_server_config_change)  # Connect button to a function

        self.passwordView = self.findChild(QtWidgets.QTextBrowser, 'passwordView')  # Find the text browser
        self.passwordView.setHtml(html_center_string + server_dict["password ="] +
                                  html_end_string)  # Show the content of variable in html form

        self.password = self.findChild(QtWidgets.QPushButton, 'password')  # Find the button
        self.password.clicked.connect(self.param_server_config_change)  # Connect button to a function

    def boolean_config_change(self):  # Universal boolean function for config file
        signal_sender = self.sender()  # Assign sender to a var
        button_name = (signal_sender.objectName())  # Get the name of sender button
        caller = str(button_name)  # Assign the name of sender button as a string
        if self.findChild(QtWidgets.QCheckBox, caller).isChecked():  # Check if checkbox is checked :)
            bool_config_content = open(config_dir, 'r')  # open cfg file with read perm.
            replacement = ""  # empty string for replacement purposes
            for config_line in bool_config_content:  # listing for function and assign a replacement line to a variable
                changes = config_line.replace(config_string + button_name + false_string, config_string + button_name +
                                              true_string)
                replacement = replacement + changes  # merge string
            bool_config_content.close()  # close config file
            file_out = open(config_dir, "w")  # open config file with write perm.
            file_out.write(replacement)  # write replacement
            file_out.close()  # close config file
        else:
            bool_config_content = open(config_dir, 'r')  # open cfg file with read perm.
            replacement = ""  # empty string for replacement purposes
            for config_line in bool_config_content:  # listing for function and assign a replacement line to a variable
                changes = config_line.replace(config_string + button_name + true_string, config_string + button_name +
                                              false_string)
                replacement = replacement + changes  # merge string
            bool_config_content.close()  # close config file
            file_out = open(config_dir, "w")  # open config file with write perm.
            file_out.write(replacement)  # write replacement
            file_out.close()  # close config file

    def boolean_server_config_change(self):  # Universal boolean function for server config file
        signal_sender = self.sender()  # Assign sender to a var
        button_name = (signal_sender.objectName())  # Get the name of sender button
        caller = str(button_name)  # Assign the name of sender button as a string
        if self.findChild(QtWidgets.QCheckBox, caller).isChecked():  # Check if checkbox is checked :)
            bool_server_content = open(server_config_dir, 'r')  # open cfg file with read perm.
            replacement = ""  # empty string for replacement purposes
            for server_config_line in bool_server_content:  # listing for fun. and assign a replacement line to a var.
                changes = server_config_line.replace(button_name + false_string, button_name + true_string)
                replacement = replacement + changes  # merge string
            bool_server_content.close()  # close config file
            file_out = open(server_config_dir, "w")  # open config file with write perm.
            file_out.write(replacement)  # write replacement
            file_out.close()  # close config file
        else:
            bool_server_content = open(server_config_dir, 'r')  # open config file with read permissions
            replacement = ""  # empty string for replacement purposes
            for server_config_line in bool_server_content:  # listing for fun. and assign a replacement line to a var.
                changes = server_config_line.replace(button_name + true_string, button_name + false_string)
                replacement = replacement + changes  # merge string
            bool_server_content.close()  # close config file
            file_out = open(server_config_dir, "w")  # open config file with write perm.
            file_out.write(replacement)  # write replacement
            file_out.close()  # close config file

    def param_config_change(self):  # Universal parameter function for config file
        signal_sender = self.sender()  # Assign sender to a var
        button_name = (signal_sender.objectName())  # Get the name of sender button
        caller = "" + str(button_name) + " ="  # Assign the name of sender button as a string with =
        user_value = askstring("Input", "Input desired value")  # get input from user through dialog
        param_config_content = open(config_dir, 'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        for config_line in param_config_content:  # listing for function and assign a replacement line to a var.
            changes = config_line.replace(config_string + button_name + " = " + config_dict[caller], config_string +
                                          button_name + " = " + user_value)
            replacement = replacement + changes  # merge string
        param_config_content.close()  # close config file
        file_out = open(config_dir, "w")  # open config file with write permissions
        file_out.write(replacement)  # write replacement
        file_out.close()  # close config file
        self.close()
        reload()
        self.__init__()
        self.show()

    def param_server_config_change(self):  # Universal parameter function for server config file
        signal_sender = self.sender()  # Assign sender to a var
        button_name = (signal_sender.objectName())  # Get the name of sender button
        caller = "" + str(button_name) + " ="  # Assign the name of sender button as a string with =
        user_value = askstring("Input", "Input desired value")  # get input from user through dialog
        param_server_content = open(server_config_dir, 'r')  # open config file with read permissions
        replacement = ""  # empty string for replacement purposes
        if str(server_dict[caller]) == "":  # check if the dictionary value is empty
            for server_config_line in param_server_content:  # listing for fun. and assign a replacement line to a var.
                changes = server_config_line.replace(button_name + " =", button_name + " = " + user_value)
                replacement = replacement + changes  # merge string
            param_server_content.close()  # close config file
        else:
            for server_config_line in param_server_content:  # listing for fun. and assign a replacement line to a var.
                changes = server_config_line.replace(button_name + " = " + server_dict[caller], button_name +
                                                     " = " + user_value)
                replacement = replacement + changes  # merge string
        param_server_content.close()  # close config file
        file_out = open(server_config_dir, "w")  # open config file with write permissions
        file_out.write(replacement)  # write replacement
        file_out.close()  # close config file
        self.close()
        reload()
        self.__init__()
        self.show()


app = QtWidgets.QApplication(sys.argv)  # defines widget
window = Ui()  # defines window
window.show()
app.exec()  # loops app
