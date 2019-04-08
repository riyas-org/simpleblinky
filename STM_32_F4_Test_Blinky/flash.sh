/usr/local/bin/openocd -f /usr/local/share/openocd/scripts/interface/stlink.cfg -f /usr/local/share/openocd/scripts/target/stm32f4x.cfg -c "program toggle.bin  0x08000000 verify reset"

