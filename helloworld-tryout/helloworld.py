from escpos.printer import Network

kitchen = Network("192.168.88.195") #Printer IP Address
kitchen.text("Hello World\n")
kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
kitchen.cut()
