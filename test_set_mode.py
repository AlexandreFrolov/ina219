import time
from ina_219_smbus import ina219_i2c

ina219=ina219_i2c(_BUS=1)

#ina219.set_cal(4096)
#ina219.set_cal(2048)
#ina219.set_config([ina219.INA219_CONFIG_GAIN_2_80MV])

raw_value=ina219.read_word(ina219.INA219_CONFIG)

hex_value = hex(raw_value)
print(f"Значение CFG в 16-ричном виде: {hex_value}")
bin_value = bin(raw_value)
print(f"Значение CFG в двоичном виде: {bin_value}")

# 0b 0011 1001 1001 1111

# Reset Bit
reset_bit = (raw_value & 0x8000) >> 15

# Bus Voltage Range
bvoltage_range = (raw_value & 0x2000) >> 13

# Gain
gain = (raw_value & 0x1800) >> 11

# Bus ADC Resolution
badc_resolution = (raw_value & 0x0780) >> 7

# Shunt ADC Resolution and Averaging
sadc_resolution = (raw_value & 0x0078) >> 3

# Operating Mode
mode = raw_value & 0x0007

# Вывод значений
print(f"Reset Bit: {reset_bit}")
print(f"Bus Voltage Range: {bvoltage_range}")
print(f"Gain: {gain}")
print(f"Bus ADC Resolution: {badc_resolution}")
print(f"Shunt ADC Resolution and Averaging: {sadc_resolution}")
print(f"Operating Mode: {mode}")


cal_raw_value=ina219.read_word(ina219.INA219_CAL)
cal_hex_value = hex(cal_raw_value)
print(f"Значение CAL в 16-ричном виде: {cal_hex_value}")
cal_bin_value = bin(cal_raw_value)
print(f"Значение CAL в двоичном виде: {cal_bin_value}")



print(ina219.get_bus_voltage(),ina219.get_current(),ina219.get_power())


#while(True):
#	print(ina219.get_bus_voltage(),ina219.get_current(),ina219.get_power())
#	time.sleep(1)
