# -*- coding: UTF-8 -*-
#A part of  WordNav addon for NVDA
#Copyright (C) 2022  Konstantin Galiakhmetov
#This file is covered by the GNU General Public License.

import appModuleHandler
import controlTypes
from logHandler import log
from NVDAObjects.JAB import JAB, JABTextInfo
import re
import textUtils
class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.Role.EDITABLETEXT:
			clsList.insert(0, CustomJAB)

class CustomJAB(JAB):
	def _get_TextInfo(self):
		if self._JABAccContextInfo.accessibleText and self.role not in [controlTypes.Role.BUTTON,controlTypes.Role.MENUITEM,controlTypes.Role.MENU,controlTypes.Role.LISTITEM]:
			return CustomJABTextInfo
		return super(JAB,self).TextInfo

class CustomJABTextInfo(JABTextInfo):
	WORD_SEPARATORS_PATTERN= r'(\W)\1*|$'

	def _getWordOffsets(self,offset):
		if not (
			self.encoding == textUtils.WCHAR_ENCODING
			or self.encoding is None
			or self.encoding == "utf_32_le"
			or self.encoding == textUtils.USER_ANSI_CODE_PAGE
		):
			raise NotImplementedError

		lineStart, lineEnd = self._getLineOffsets(offset)
		lineText = self._getTextRange(offset,lineEnd)
		# Convert NULL and non-breaking space to space to make sure that words will break on them
		lineText = lineText.translate({0:u' ',0xa0:u' '})
		if not lineText:
			return (offset, offset+1)
		separator =re.search(self.WORD_SEPARATORS_PATTERN, lineText)
		wordLen =separator.start() if self._isPunctuation(lineText[0 	]) else separator.end()
		return (offset, offset+wordLen)

	def _isPunctuation(self, s):
		 return re.fullmatch(self.WORD_SEPARATORS_PATTERN, s) == None
