'''
Standalone class to handle daemonisation.
'''

from abc import ABC, abstractmethod
import os
import signal
import sys

import typing
from pydantic import BaseModel

class Daemoniser:
	@staticmethod
	def daemonise() -> None:
		Daemoniser.__resetSignals()
		Daemoniser.__resetSignalMask()

		Daemoniser.__sanitiseEnv()
		Daemoniser.__closeFd()

		Daemoniser.__forkAndExit()
		os.setsid()
		Daemoniser.__forkAndExit()

	@staticmethod
	def __resetSignals() -> None:
		# Clear signal handlers
		for sig in range(1, signal.NSIG): # Iterate via avalible signums
			try:
				signal.signal(sig, signal.SIG_DFL) # Clear anything that pop up
			except (OSError, RuntimeError):
				pass
				
	@staticmethod
	def __resetSignalMask() -> None:
		signal.pthread_sigmask(signal.SIG_SETMASK,[])
		return

	@staticmethod
	def __sanitiseEnv() -> None:
		return
	@staticmethod
	def __closeFd() -> None:
		return
	@staticmethod
	def __forkAndExit() -> None:
		# This will immediately exit parent and keep child running
		pid: int = os.fork()
		if pid > 0:
			os._exit(0)
	@staticmethod
	def __redirectStdio() -> None:
		return
	@staticmethod
	def __finalizeDaemon() -> None:
		return
