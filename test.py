import pymodbus
#from pymodbus.client.sync import ModbusSerialClient as modclient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.register_read_message import ReadInputRegistersRequest
#from pymodbus.register_read_message import ReadHoldingRegistersRequest
#from pymodbus.framer.rtu_framer import ModbusRtuFramer

client = ModbusClient('localhost', port=5020)
# client1 = modclient(method='tcp', port='/dev/ttyUSB0', stopbits=1, bytesize=8, baudrate=19200)

conn = client1.connect()
print(conn)

rq = client1.write_register(257, 0, unit=0x01)
rr = client1.read_holding_registers(257, 1, unit=0x01)
print rr.registers
