# Maximo 7.6.x automation script to create bulletin board message

from psdi.app.bulletinboard import BBSet 
from psdi.server import MXServer
from java.util import Calendar
from psdi.mbo import MboConstants

service.log(scriptName + " [BEGIN]")

mxServer = MXServer.getMXServer()

userInfo = mbo.getUserInfo()

curDate = mxServer.getDate()
calendar = Calendar.getInstance()
calendar.add(Calendar.DATE, 7)
expDate = calendar.getTime()

bulletinSet = mxServer.getMboSet("BULLETINBOARD",mxServer.getUserInfo("MAXADMIN"))
bulletin = bulletinSet.add()
bulletin.setValue("SUBJECT","A high priority PO was assigned to you for review")
bulletin.setValue("MESSAGE","see PO AB12345 ")
bulletin.setValue("POSTDATE",curDate)
bulletin.setValue("EXPIREDATE",expDate)
bulletin.setValue("STATUS","APPROVED", MboConstants.NOVALIDATION_AND_NOACTION | MboConstants.NOACCESSCHECK)

bulletinId = bulletin.getString("BULLETINBOARDID")
service.log(scriptName + " [BULLETINID] " + str(bulletinId))

bulletinSet.save()

bulletinAudienceSet = bulletin.getMboSet("BBAUD")
bulletinAudience = bulletinAudienceSet.add()

bulletinAudience.setValue("BULLETINBOARDID",bulletinId)
bulletinAudience.setValue("PERSONGROUP","MAXADMIN")

bulletinAudienceSet.save()

bulletinStatusSet = bulletin.getMboSet("BBSTATUSHISTORY")
bulletinStatus = bulletinStatusSet.add()

bulletinStatus.setValue("BULLETINBOARDID",bulletinId)
bulletinStatus.setValue("CHANGEDATE",curDate)
bulletinStatus.setValue("CHANGEDBY","MAXADMIN")
bulletinStatus.setValue("STATUS","APPROVED")

bulletinStatusSet.save()

status = bulletin.getString("STATUS")

print(scriptName + " [STATUS]: " + str(status))

service.log(scriptName + ": [END]")
