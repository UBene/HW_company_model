'''
Created on Jan 20, 2025

@author: Benedikt Ursprung
'''
# from time import time

from ScopeFoundry.hardware import HardwareComponent


class ModelHw(HardwareComponent):

    name = "model"

    def setup(self):
        s = self.settings
        s.New("port", str, initial="COM1",
              description='COMx see device manager')
        s.New("property_x", float, ro=False, unit='mm', spinbox_decimals=4, si=False)


    def connect(self):

        S = self.settings

        from .model_dev import ModelDev
        self.dev = ModelDev(S["port"], debug=S['debug_mode'])

        # bind read and/or write functions to a setting (sometimes only one is applicable)
        S.get_lq("property_x").connect_to_hardware(
            read_func=self.dev.read_property_x, write_func=self.dev.write_property_x
        )

    def disconnect(self):
        if not hasattr(self, 'dev'):
            return

        # self.settings.disconnect_all_from_hardware()
        self.dev.close()
        del self.dev

    # if you want to continuously update settings implement *run* method
    # def run(self):
    #     self.settings.property_x.read_from_hardware()
    #     time.sleep(0.1)
