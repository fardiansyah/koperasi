from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import odoorpc
import base64
import imghdr
import io

pointer = 0
total_rec = 0

class MyWidget(BoxLayout):
    nama_text = StringProperty("Test")

    def on_start

    def update_prev(self):
        global pointer, im
        if pointer > 0:
            pointer -= 1
        print pointer
        order = Merk.browse(merk_ids[pointer])
        data = base64.b64decode(order.image)
        dataio = io.BytesIO(data)
        img_type = imghdr.what('', data)
        im = CoreImage(dataio, ext=img_type)
        self.nama_text = order.name
        gbr = self.ids['gambar']
        gbr.texture = im.texture

    def update_next(self):
        global pointer, im, total_rec
        if pointer < total_rec:
            pointer += 1
        print pointer, total_rec
        order = Merk.browse(merk_ids[pointer])
        if order.image != False:
            data = base64.b64decode(order.image)
        else:
            data = open('no-image.png','rb').read()
        dataio = io.BytesIO(data)
        img_type = imghdr.what('', data)
        im = CoreImage(dataio, ext=img_type)
        self.nama_text = order.name
        gbr = self.ids['gambar']
        gbr.texture = im.texture


class OdooApp(App):
    global Merk, merk_ids, im, total_rec
    pointer = 0
    odoo = odoorpc.ODOO('localhost', port=8068)
    odoo.login('demo10', 'admin', 'admin')
    Merk = odoo.env['res.partner']
    merk_ids = Merk.search([])
    order = Merk.browse(merk_ids[pointer])
    data = base64.b64decode(order.image)
    dataio = io.BytesIO(data)
    img_type = imghdr.what('', data)
    im = CoreImage(dataio, ext=img_type)
    #gbr.texture = im.texture
    #self.nama_text = order.name
    total_rec = len(merk_ids) - 1
    print "here"

    def build(self):
        return MyWidget()



if __name__ == '__main__':
    OdooApp().run()

