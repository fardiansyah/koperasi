from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.image import Image as CoreImage
import odoorpc
import base64
import imghdr
import io

class MerkScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MerkScreen,self).__init__(**kwargs)
        self.cols = 2
        odoo = odoorpc.ODOO('localhost', port=8068)
        odoo.login('koperasi','admin','admin')
        Merk = odoo.env['ksp.jaminan.merk']
        merk_ids = Merk.search([])
        order = Merk.browse(merk_ids[2])
        data = base64.b64decode(order.image)
        dataio = io.BytesIO(data)
        img_type=imghdr.what('',data)
        im = CoreImage(dataio,ext=img_type)
        self.add_widget(Image(name='merk',texture=im.texture))
        self.add_widget(Label(text=order.name))
        self.add_widget(Button(text='Prev'))
        self.add_widget(Button(text='Next'))

    def update_image(self):
        order = Merk.browse(merk_ids[2])
        data = base64.b64decode(order.image)
        dataio = io.BytesIO(data)
        img_type=imghdr.what('',data)
        im = CoreImage(dataio,ext=img_type)
        self.merk.texture=im.texture

class OdooApp(App):
    def build(self):
        return MerkScreen()

if __name__ == '__main__':
    OdooApp().run()

