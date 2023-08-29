# The header is present. 
# The visualisation is present.
# The region picker is present. 


import pytest
from dash.testing.application_runners import import_app
from dash.testing.application_runners import DashComposite
import warnings
import xarray

# Import the names of callback functions you want to test
from vagabond_task4 import app

@pytest.fixture
def app_instance():
    return import_app(app)

def test_header_exists(dash_duo, app_instance, capsys):
    dash_duo.start_server(app_instance)
    with capsys.disabled():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        dash_duo.wait_for_element("#header", timeout=15)

def test_region_picker_exists(dash_duo, app_instance, capsys):
    dash_duo.start_server(app_instance)
    with capsys.disabled():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        dash_duo.wait_for_element("#region_picker", timeout=15)

def test_visualize_exists(dash_duo, app_instance, capsys):
    dash_duo.start_server(app_instance)
    with capsys.disabled():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        dash_duo.wait_for_element("#vis", timeout=15)