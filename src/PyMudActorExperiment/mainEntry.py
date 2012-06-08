'''
Created on Nov 20, 2011

@author: Nich
'''
import unittest
from mail_sorter import MailSorter
from queue import Queue
import commands.commands as comm
from commands.commandIO import my_input
from commands.command_picker import command_picker


if __name__ == '__main__':
    mail_queue = Queue()
    sorter = MailSorter(mail_queue)
    m_in = my_input(command_picker(sorter.inbox()))
    while True:
        line = input("->")
        m_in.send(line)
        sorter.run()
        sorter.run()
        sorter.run()
        sorter.run()
        sorter.run()
        sorter.run()
        