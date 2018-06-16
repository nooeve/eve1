# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("ป้อน PIN นี้ '" + pin + "' Bot PY.3 By. SAI")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='或掃描此QR '
        else:
            notice=''
        self.callback('Self ' + notice + ' Bot PY.3 By. SAI\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
