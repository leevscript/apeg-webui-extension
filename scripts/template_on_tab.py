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
    with gr.Blocks(analytics_enabled=False) as apeg_tab:
        # Check if Controlnet is installed and enabled in settings, so we can show or hide the "Send to Controlnet" buttons.
        controlnet_exists = False
        for extension in extensions.active():
            if "controlnet" in extension.name:
                controlnet_exists = True
                break

        with gr.Row():
            # Add an iframe with Photopea directly in the tab.
            gr.HTML(
                f"""<iframe id="{PHOTOPEA_IFRAME_ID}"
                src = "{PHOTOPEA_MAIN_URL}"
                width = "{PHOTOPEA_IFRAME_WIDTH}"
                height = "{PHOTOPEA_IFRAME_HEIGHT}"
                onload = "{PHOTOPEA_IFRAME_LOADED_EVENT}(this)">"""
            )

    return [(apeg_tab, "Apeg", "apeg_embed")]

# Actually hooks up the tab to the WebUI tabs.
script_callbacks.on_ui_tabs(on_ui_tabs)