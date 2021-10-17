# Automation script for Maximo 7.6.x to generate a QR code for a newly created asset,
# save the QR code image to the doclinks folder on the server and create docinfo and doclinks
# records to attach the image to the asset record in Maximo

from psdi.iface.router import HTTPHandler
from java.util import HashMap

api_url = 'http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://maximo.wiki'
assetNum = mbo.getString("ASSETNUM")

fName ='asset_' + assetNum + '.png'
fullFName ='c:/doclinks/qrcodes/asset_' + assetNum + '.png'

handler = HTTPHandler()
map = HashMap()
map.put("URL",api_url)
map.put("HTTPMETHOD","GET")
try:
    resBytes = handler.invoke(map,None)
    imgFile = open(fullFName,'ab')
    imgFile.write(resBytes)
    imgFile.flush()
    imgFile.close()
except MXException, e:
    service.log('error: ', e)

docLinksSet = mbo.getMboSet("DOCLINKS")
docLink = docLinksSet.add()
docLink.setValue("AddInfo",True)
docLink.setValue("DESCRIPTION","Asset " + assetNum + " QR Code")
docLink.setValue("DOCUMENT",fName)
docLink.setValue("NEWURLNAME",fName)
docLink.setValue("URLNAME",fName)
docLink.setValue("URLTYPE","FILE")
docLink.setValue("DOCTYPE","QRCODES")

service.log('FIN')
