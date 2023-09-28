# This is a sample Python script.
import asyncio
import sys
from Application import ApplicationMain
import uvloop
import click
import commands
import os, sys
import traceback
import logging
from click.parser import split_arg_string
import stdconsole
from gpiozero.devices import Device
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.pins.mock import MockFactory

# import module
import purify as pr
import time
import flagger as fg


@ApplicationMain
async def main():    
    logger = logging.getLogger().getChild("command")
    ######### START USER DEFINED PY ########
    
    myMessage = pr.main(True)
    print(myMessage)
    time.sleep(1) ## Time Delay 고려
    myFlag = fg.main(1, "TURBIN")
    print(myFlag)
    time.sleep(1)
    myNewMessage = pr.main(False)
    print(myNewMessage)
    time.sleep(1)

    ##### END OF THE USER DEFINED PY #####
    await commands.run_command(None)
    async for message in stdconsole.input_sequence():
        if message == 'exit':
            break
        args = split_arg_string(message)
        
        if args is None or len(args) < 1:
            click.echo("wrong command input", err=True)
            continue
        try:
            await commands.run_command(args)
        except click.UsageError as err:
            logger.exception(err)
            click.echo(message=err, err=True)
    raise sys.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvloop.install()
    Device.pin_factory = PiGPIOFactory(host='192.168.0.90')
    #Device.pin_factory = MockFactory()
    try:
        main(debug=True)
    finally:
        if not Device.pin_factory is None:
            try:
                Device.pin_factory.close()
            except:
                pass
    