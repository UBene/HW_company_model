'''
Created on Jan 20, 2025

@author: Benedikt Ursprung
'''

from ScopeFoundry.base_app import BaseMicroscopeApp


class TestApp(BaseMicroscopeApp):

    name = "model_test_app"

    def setup(self):
        
        from ScopeFoundryHW.company_model import ModelHw, ModelReadout
        self.add_hardware(ModelHw(self))
        self.add_measurement(ModelReadout(self))



if __name__ == '__main__':
    import sys
    app = TestApp(sys.argv)
    sys.exit(app.exec_())
