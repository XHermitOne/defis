# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.calendar
from STD.usercomponents import icyearchoicectrl
from STD.usercomponents import icmonthchoicectrl

###########################################################################
## Class calendarDialogProto
###########################################################################

class calendarDialogProto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Календарь", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.calendarCtrl = wx.calendar.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_SHOW_HOLIDAYS )
		bSizer1.Add( self.calendarCtrl, 0, wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.cancelButton, 0, wx.ALL, 5 )
		
		self.okButton = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.okButton, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.onCancelButtonClick )
		self.okButton.Bind( wx.EVT_BUTTON, self.onOkButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCancelButtonClick( self, event ):
		event.Skip()
	
	def onOkButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class yearDialogProto
###########################################################################

class yearDialogProto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Выбор года", pos = wx.DefaultPosition, size = wx.Size( 351,110 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Год:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearChoiceControl = icyearchoicectrl.icYearChoiceCtrl(self, -1, {})
		bSizer5.Add( self.yearChoiceControl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.cancelButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.okButton = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.okButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( bSizer4, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.onCancelButtonClick )
		self.okButton.Bind( wx.EVT_BUTTON, self.onOkButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCancelButtonClick( self, event ):
		event.Skip()
	
	def onOkButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class monthDialogProto
###########################################################################

class monthDialogProto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Выбор месяца", pos = wx.DefaultPosition, size = wx.Size( 390,110 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Месяц:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer7.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.monthChoiceControl = icmonthchoicectrl.icMonthChoiceCtrl(self, -1, {})
		bSizer7.Add( self.monthChoiceControl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearChoiceControl = icyearchoicectrl.icYearChoiceCtrl(self, -1, {})
		bSizer7.Add( self.yearChoiceControl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cancelButton, 0, wx.ALL, 5 )
		
		self.okButton = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.okButton, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.onCancelButtonClick )
		self.okButton.Bind( wx.EVT_BUTTON, self.onOkButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCancelButtonClick( self, event ):
		event.Skip()
	
	def onOkButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class monthRangeDialogProto
###########################################################################

class monthRangeDialogProto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Выбор периода", pos = wx.DefaultPosition, size = wx.Size( 393,165 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"с:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.monthFirstChoiceControl = icmonthchoicectrl.icMonthChoiceCtrl(self, -1, {})
		fgSizer1.Add( self.monthFirstChoiceControl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearFirstChoiceControl = icyearchoicectrl.icYearChoiceCtrl(self, -1, {})
		fgSizer1.Add( self.yearFirstChoiceControl, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"по:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer1.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.monthLastChoiceControl = icmonthchoicectrl.icMonthChoiceCtrl(self, -1, {})
		fgSizer1.Add( self.monthLastChoiceControl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearLastChoiceControl = icyearchoicectrl.icYearChoiceCtrl(self, -1, {})
		fgSizer1.Add( self.yearLastChoiceControl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cancelButton, 0, wx.ALL, 5 )
		
		self.okButton = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.okButton, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.onCancelButtonClick )
		self.okButton.Bind( wx.EVT_BUTTON, self.onOkButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCancelButtonClick( self, event ):
		event.Skip()
	
	def onOkButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dateRangeDialogProto
###########################################################################

class dateRangeDialogProto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Выбор периода", pos = wx.DefaultPosition, size = wx.Size( 393,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.AddGrowableRow( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"с:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.firstDatePicker = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer2.Add( self.firstDatePicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"по:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer2.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lastDatePicker = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer2.Add( self.lastDatePicker, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer6.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cancelButton, 0, wx.ALL, 5 )
		
		self.okButton = wx.Button( self, wx.ID_ANY, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.okButton, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.onCancelButtonClick )
		self.okButton.Bind( wx.EVT_BUTTON, self.onOkButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCancelButtonClick( self, event ):
		event.Skip()
	
	def onOkButtonClick( self, event ):
		event.Skip()
	

