import pymodbus
from pymodbus.client.sync import ModbusSerialClient as modclient
from pymodbus.register_read_message import ReadInputRegistersRequest
from pymodbus.register_read_message import ReadHoldingRegistersRequest
from pymodbus.framer.rtu_framer import ModbusRtuFramer


client1 = modclient(method='rtu', port='/dev/ttyUSB0', stopbits=1, bytesize=8, baudrate=19200)

conn = client1.connect()
print(conn)

rq = client1.write_register(257, 0, unit=0x01)
rr = client1.read_holding_registers(257, 1, unit=0x01)
print rr.registers
