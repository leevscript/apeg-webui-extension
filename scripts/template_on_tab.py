import gradio as gr
from modules import script_callbacks
from modules.shared import opts
from modules import extensions


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as apeg_tab:
        with gr.Row():
            gr.HTML(
                f"""<iframe id="webui-apeg-iframe"
                src = "https://apeg.cn/teleprompter?source=webui"
                width = "100%"
                height = "768">"""
            )

    return [(apeg_tab, "Apeg", "apeg_embed")]

script_callbacks.on_ui_tabs(on_ui_tabs)