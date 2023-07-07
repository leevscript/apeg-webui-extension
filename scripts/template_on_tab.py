import gradio as gr
from modules import script_callbacks
from modules.shared import opts
from modules import extensions

# Handy constants
PHOTOPEA_MAIN_URL = "https://www.apeg.cn?from=webui"
PHOTOPEA_IFRAME_ID = "webui-photopea-iframe"
PHOTOPEA_IFRAME_HEIGHT = 768
PHOTOPEA_IFRAME_WIDTH = "100%"
PHOTOPEA_IFRAME_LOADED_EVENT = "onPhotopeaLoaded"


# Adds the "Apeg" tab to the WebUI
def on_ui_tabs():
    gr.HTML(
        f"""<iframe id="{PHOTOPEA_IFRAME_ID}"
        src = "{PHOTOPEA_MAIN_URL}"
        width = "{PHOTOPEA_IFRAME_WIDTH}"
        height = "{PHOTOPEA_IFRAME_HEIGHT}"
        onload = "{PHOTOPEA_IFRAME_LOADED_EVENT}(this)">"""
    )

    return [(photopea_tab, "Apeg", "apeg_embed")]

# Actually hooks up the tab to the WebUI tabs.
script_callbacks.on_ui_tabs(on_ui_tabs)