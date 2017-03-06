import serial                    # import pySerial module

	def getweight(self):
		try:

			ComPort = serial.Serial('COM3') # open the COM Port
			ComPort.baudrate = 2400          # set Baud rate
			ComPort.bytesize = 8             # Number of data bits = 8
			ComPort.parity   = 'N'           # No parity
			ComPort.stopbits = 1             # Number of Stop bits = 1
			data = ComPort.read(8)        # Wait and read data
			a=int(data[-6:])
			if(type(a) is int):
				ComPort.close()    
				print(a)
	
		except:
			print("lol")