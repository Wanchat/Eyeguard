# from win32com.client import GetObject
# objWMI = GetObject('winmgmts:\\\\.\\root\\WMI').InstancesOf('WmiMonitorID')

# for obj in objWMI:
# 	if obj.Active != None:
# 		print("Active:" + str(obj.Active))
# 	if obj.InstanceName != None:
# 		print("InstanceName:" + str(obj.InstanceName))
# 	if obj.ManufacturerName != None:
# 		print("ManufacturerName:" + str(obj.ManufacturerName))
# 	if obj.ProductCodeID != None:
# 		print("ProductCodeID:" + str(obj.ProductCodeID))
# 	if obj.SerialNumberID != None:
# 		print("SerialNumberID:" + str(obj.SerialNumberID))
# 	if obj.UserFriendlyName != None:
# 		print("UserFriendlyName:" + str(obj.UserFriendlyName))
# 	if obj.UserFriendlyNameLength != None:
# 		print("UserFriendlyNameLength:" + str(obj.UserFriendlyNameLength))
# 	if obj.WeekOfManufacture != None:
# 		print("WeekOfManufacture:" + str(obj.WeekOfManufacture))
# 	if obj.YearOfManufacture != None:
# 		print("YearOfManufacture:" + str(obj.YearOfManufacture))
# 	print("")
# 	print("########")
# 	print("")

# import winreg

# path = r'Control Panel\Desktop\PerMonitorSettings'
# areg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
# akey = winreg.OpenKey(areg, path)
# mointor_id = winreg.EnumKey(akey,1)

# path = path+r"\{}".format(mointor_id)
# path_2 = r'Control Panel\Desktop\PerMonitorSettings\CMN14D60_2A_07E0_9A^798E14FD3DC52A476638687F5814BFF0\test'

# open_key = winreg.OpenKey(areg, path,0,winreg.KEY_WRITE)

# winreg.SetValueEx(open_key,"DpiValue",0,winreg.REG_DWORD,1)

# print (path)
# ms-settings:display

import os

os.system("start ms-settings:display")
