### Source: https://aiosmtpd.readthedocs.io/

import asyncio
from aiosmtpd.controller import Controller
import time


class ExampleHandler:

    async def handle_RCPT(self, server, session, envelope, address: str, rcpt_options):
        print(address)
        if not address.endswith('@example.com'):
            return '550 not relaying to that domain'
        print(envelope)
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            print(f'> {ln}'.strip())
        print()
        print('End of message')
        return '250 Message accepted for delivery'


controller = Controller(ExampleHandler(), hostname="0.0.0.0")
controller.start()
while True:
    time.sleep(0.01)
