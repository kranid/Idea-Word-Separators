# -*- coding: UTF-8 -*-
#A part of  WordNav addon for NVDA
#Copyright (C) 2022  Konstantin Galiakhmetov
#This file is covered by the GNU General Public License.



import appModuleHandler
import globalPluginHandler
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		appModuleHandler.registerExecutableWithAppModule("studio64", "ideawordseparators")
		appModuleHandler.registerExecutableWithAppModule("idea64", "ideawordseparators")

	def terminate(self, *args, **kwargs):
		super().terminate(*args, **kwargs)
		appModuleHandler.unregisterExecutable("studio64")
		appModuleHandler.unregisterExecutable("idea64")