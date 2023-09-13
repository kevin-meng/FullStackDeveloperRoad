
import gradio as gr 
import whisper
from utils import translate
from functools import partial

output_types = ['txt','vtt','srt','json','tsv']
model = whisper.load_model("medium")
translate_to_srt = partial(translate, model=model)


block = gr.Blocks()

with block:
    gr.Markdown("# 🌆 音视频处理")
    with gr.Row(): 
        with gr.Column() as col1:
            with gr.Box(): 
                with gr.Row().style():
                    inp_video = gr.Video(
                        label="输入视频",
                        type="filepath",
                        mirror_webcam = False
                    )
            # out_format = gr.CheckboxGroup(output_types,label="输出文本类型")
            out_format = gr.Dropdown(output_types,label="输出文本类型")

        with gr.Column():
            with gr.Tab("字幕"):
                op_text = gr.Textbox(lines=11)
            with gr.Tab("视频"):
                op_video = gr.Video() 
                gr.Markdown("视频添加字幕")   
            with gr.Tab("音频"):
                op_audio = gr.Audio()                    

        with col1:
            btn = gr.Button("提取视频字幕")
            btn.click(translate_to_srt, inputs=[inp_video,out_format], outputs=[op_video, op_text, op_audio]) 
        

    gr.HTML('''
    <div class="footer">
                <p>Model by <a href="https://github.com/openai/whisper" style="text-decoration: underline;" target="_blank">OpenAI</a> 
                </p>
    </div>
    ''')


if __name__ == "__main__":
    block.launch()  # debug = True
