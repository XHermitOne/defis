#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Класс пользовательского компонента COM Клиент.

@type ic_user_name: C{string}
@var ic_user_name: Имя пользовательского класса.
@type ic_can_contain: C{list | int}
@var ic_can_contain: Разрешающее правило - список типов компонентов, которые
    могут содержаться в данном компоненте. -1 - означает, что любой компонент
    может содержатся в данном компоненте. Вместе с переменной ic_can_not_contain
    задает полное правило по которому определяется возможность добавления других 
    компонентов в данный комопнент. 
@type ic_can_not_contain: C{list}
@var ic_can_not_contain: Запрещающее правило - список типов компонентов, 
    которые не могут содержаться в данном компоненте. Запрещающее правило
    начинает работать если разрешающее правило разрешает добавлять любой 
    компонент (ic_can_contain = -1).
"""

import wx
import ic.components.icwidget as icwidget
import ic.utils.util as util
import ic.components.icResourceParser as prs
import ic.imglib.common as common
import ic.PropertyEditor.icDefInf as icDefInf

import ic.db.icCOMClient as ic_comclient

#   Тип компонента
ic_class_type = icDefInf._icDatasetType

#   Имя класса
ic_class_name = 'icCOMClient'

#   Описание стилей компонента
ic_class_styles = {'DEFAULT':0}

#   Спецификация на ресурсное описание класса
ic_class_spc = {'__events__': {}, 
                'type': ic_comclient.COMCLIENT_TYPE, 
                'name': 'default', 
                'activate':1,
                'init_expr':None,
                '_uuid':None,
                '__attr_types__': {icDefInf.EDT_TEXTFIELD: ['name', 'type']}, 
                '__parent__':ic_comclient.SPC_IC_COMCLIENT, 
               }
                    
ic_class_spc['__styles__'] = ic_class_styles

#   Имя иконки класса, которые располагаются в директории 
#   ic/components/user/images
ic_class_pic = '@common.imgEdtCOMClient'
ic_class_pic2 = '@common.imgEdtCOMClient'

#   Путь до файла документации
ic_class_doc = 'ic/doc/ic.components.user.ic_comclient_wrp.icCOMClient-class.html'
ic_class_spc['__doc__'] = ic_class_doc
                    
#   Список компонентов, которые могут содержаться в компоненте
ic_can_contain = []

#   Список компонентов, которые не могут содержаться в компоненте, если не определен 
#   список ic_can_contain
ic_can_not_contain = None

#   Версия компонента
__version__ = (0,0,0,1)

class icCOMClient(icwidget.icSimple,ic_comclient.icCOMClientPrototype):
    """
    COM клиент.
    """
    #Спецификаци компонента
    component_spc = ic_class_spc
    
    def __init__(self, parent, id=-1, component=None, logType = 0, evalSpace = None,
                        bCounter=False, progressDlg=None):
        """
        Конструктор.

        @type parent: C{wx.Window}
        @param parent: Указатель на родительское окно
        @type id: C{int}
        @param id: Идентификатор окна
        @type component: C{dictionary}
        @param component: Словарь описания компонента
        @type logType: C{int}
        @param logType: Тип лога (0 - консоль, 1- файл, 2- окно лога)
        @param evalSpace: Пространство имен, необходимых для вычисления внешних выражений
        @type evalSpace: C{dictionary}
        @type bCounter: C{bool}
        @param bCounter: Признак отображения в ProgressBar-е. Иногда это не нужно -
            для создания объектов полученных по ссылки. Т. к. они не учтены при подсчете
            общего количества объектов.
        @type progressDlg: C{wx.ProgressDialog}
        @param progressDlg: Указатель на идикатор создания формы.
        """
        component = util.icSpcDefStruct(self.component_spc, component)
        icwidget.icSimple.__init__(self,parent,id,component,logType,evalSpace)
        ic_comclient.icCOMClientPrototype.__init__(self,component)

    def getData(self,*args,**kwargs):
        """
        Функция получения данных из COM сервера.
        """
        return self.getICAttr('get_data')
        
    def setData(self,*args,**kwargs):
        """
        Функция сохранения данных в COM сервере.
        """
        return self.getICAttr('set_data')

