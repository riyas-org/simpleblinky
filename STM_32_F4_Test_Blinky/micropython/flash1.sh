/usr/local/bin/openocd -f /usr/local/share/openocd/scripts/interface/stlink.cfg -f /usr/local/share/openocd/scripts/target/stm32f4x.cfg -c "program firmware1.bin  0x08020000  verify reset"

