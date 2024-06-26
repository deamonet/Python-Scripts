#
# Python Port Scanner
#
import wx                   # import the GUI model wx
import sys                  # import the standard lirbrary module sys
import ping              # import the icmp Ping Module
from socket import *    # import the standard library module socket

from time import gmtime, strftime # import time functions

#
# Event Handler for the portScan Button Press
#

def portScan(event):
    #First, I need to check that the starting port is <= ending port value
    if portEnd.GetValue() < portStart.GetValue():
        # This is an improper setting
        # Notify the user and return

        dlg = wx.MessageDialog(mainWin, "Invalid Host Port Selection",
                               "Confirm", wx.OK|wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return
    #update the Status Bar
    mainWin.StatusBar.SetStatusText('Executing Port Scan . . . .. Please Wait')

    #Record the Start Time
    utcStart = gmtime()
    utc = strftime("%a, %d %b %Y %X + 0000", utcStart)
    results.AppendText("\n\nPort Scan Started: "+utc+ "\n\n")

    # Build the base IP Address String
    # Extract data from the ip Range and host name user selections
    # Build a Python List of IP Addresses to Sweep

    baseIP = str(ipaRange.GetValue())+'.'+str(ipbRange.GetValue())+'.'+str(ipcRange.GetValue())+'.'+str(ipdRange.GetValue())

    # For the IP Addresses Specified, Scan the Ports Specified
    for port in range (portStart.GetValue(), portEnd.GetValue()+1):
        try:
            # Report the IP Address to the Window Status Bar
            mainWin.StatusBar.SetStatusText('Scanning: ' + baseIP + ' Port: '+str(port))
            # Open a socket
            reqSocket = socket(AF_INET, SOCK_STREAM)
            # Try connecting to the specified IP, Port
            response = reqSocket.connect_ex((baseIP, port))
            # if we receive a proper response from the port
            # then display the results received
            # print response *testing purposes*
            if response == 0:
                # Display the ipAddress and Port
                results.AppendText(baseIP+'\t'+str(port)+'\t')
                results.AppendText('Open')
                results.AppendText("\n")
            else:
                # if the result failed, only display the result
                # when the user has selected the "Display All" check box
                if displayAll.GetValue() == True:
                    results.AppendText(baseIP+'\t'+str(port)+'\t')
                    results.AppendText('Closed')
                    results.AppendText("\n")
                # Close the socket
            reqSocket.close()
        except socket.error as e:
            # for socket Errors Report the offending IP
            results.AppendText(baseIP+'\t'+str(port)+'\t')
            results.AppendText('Failed: ')
            results.AppendText(e.message)
            results.AppendText("\n")
    # Record and display the ending time of the sweep
    utcEnd = gmtime()
    utc = strftime("%a, %d %b %Y %X +0000", utcEnd)
    results.AppendText("\nPort Scan Ended: "+utc+"\n\n")

    # Clear the Status Bar
    mainWin.StatusBar.SetStatusText('')

# End Scan Event Handler

#
# Program Exit Handler =================================
#

def programExit(event):
    sys.exit()
# End Program Exit Handle ==============================

#
# Setup the Application Windows ==========================
#

app = wx.App()

# define window
mainWin = wx.Frame(None, title = "Simple Port Scanner", size = (1200, 600))

# define the action panel
panelAction = wx.Panel(mainWin)

# define action buttons
# I'm creating two buttons, one for Scan and one for Exit
# Notice that each button contains the name of the function that will
# handle the button press event. Port Scan and Program Exit respectively

displayAll = wx.CheckBox(panelAction, -1, 'Display All', (10,10))
displayAll.SetValue(True)

scanButton = wx.Button(panelAction, label = 'Scan')
scanButton.Bind(wx.EVT_BUTTON, portScan)

exitButton = wx.Button(panelAction, label = 'Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

# define a Text Area where I can display results
results = wx.TextCtrl(panelAction, style = wx.TE_MULTILINE | wx.HSCROLL)

# Base Network for Classic C IP Address has 3 components
# For class C addresses, the first 3 octets define the network i.e 127.0.0
# The last 8 bits define the host i.e. 0-255

# Thus I setup 3 spin controls one for each of the 4 network octets
# I also, set the default value to 127.0.0.0 for convenience
ipaRange = wx.SpinCtrl(panelAction, -1, '')
ipaRange.SetRange(0,255)
ipaRange.SetValue(127)

ipbRange = wx.SpinCtrl(panelAction, -1, '')
ipbRange.SetRange(0,255)
ipbRange.SetValue(0)

ipcRange = wx.SpinCtrl(panelAction, -1, '')
ipcRange.SetRange(0,255)
ipcRange.SetValue(0)

ipdRange = wx.SpinCtrl(panelAction, -1, '')
ipdRange.SetRange(0,255)
ipdRange.SetValue(1)

# Add a label for clarity
ipLabel = wx.StaticText(panelAction, label = "IP Address: ")

# Next, I want to provide the user with the ability to set the port range
# they wish to scan. Maximum is 20 - 1025
portStart = wx.SpinCtrl(panelAction, -1, '')
portStart.SetRange(1, 1025)
portStart.SetValue(1)

portEnd = wx.SpinCtrl(panelAction, -1, '')
portEnd.SetRange(1, 1025)
portEnd.SetValue(5)

PortStartLabel = wx.StaticText(panelAction, label = "Port Start: ")
PortEndLabel = wx.StaticText(panelAction, label = "Port End: ")

# Now I create BoxSizer to automatically align the different components neatly
# First, I create a horizontal Box
# I'm adding the buttons, ip Range and Host Spin Controls
actionBox = wx.BoxSizer()

actionBox.Add(displayAll, proportion = 0, flag = wx.LEFT | wx.CENTER, border = 5)
actionBox.Add(scanButton, proportion = 0, flag = wx.LEFT, border = 5)
actionBox.Add(exitButton, proportion = 0, flag = wx.LEFT, border = 5)

actionBox.Add(ipLabel, proportion = 0, flag = wx.LEFT | wx.CENTER, border = 5)

actionBox.Add(ipaRange, proportion = 0, flag = wx.LEFT, border = 5)
actionBox.Add(ipbRange, proportion = 0, flag = wx.LEFT, border = 5)
actionBox.Add(ipcRange, proportion = 0, flag = wx.LEFT, border = 5)
actionBox.Add(ipdRange, proportion = 0, flag = wx.LEFT, border = 5)

actionBox.Add(PortStartLabel, proportion = 0, flag = wx.LEFT | wx.CENTER, border = 5)
actionBox.Add(portStart, proportion = 0, flag = wx.LEFT, border = 5)

actionBox.Add(PortEndLabel, proportion = 0, flag = wx.LEFT | wx.CENTER, border = 5)
actionBox.Add(portEnd, proportion = 0, flag = wx.LEFT, border = 5)

# Next I create a Vertical Box that I place the Horizontal Box components
# inside along with the results text area
vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vertBox.Add(results, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

# I'm adding a menu and status bar to the main window

# Finally, I use the SetSizer function to automatically size the windows
# based on the definitions above
panelAction.SetSizer(vertBox)
mainWin.CreateStatusBar()
#Display the main window
mainWin.Show()
# Enter the Applications Main Loop
# Awaiting User Actions
app.MainLoop()