

import os
import whisper

#from moviepy.editor import VideoFileClip


def video2mp3(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    # subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
    #                 stdout=subprocess.DEVNULL,
    #                 stderr=subprocess.STDOUT)
    os.system(f"ffmpeg -y -i {video_file} {filename}.{output_ext}")
    return f"{filename}.{output_ext}"


def audio2srt(audio_file,model,output_types,input_name,home_path):
    # 抽取字幕
    options = dict(beam_size=5, best_of=5)
    translate_options = dict(task="translate", **options)
    result = model.transcribe(audio_file,**translate_options)

    # 视频字幕合成
    for tp in output_types:
        writer = whisper.utils.get_writer(tp, home_path)
        subtitle =  f"{input_name}.{tp}"
        writer(result, rf"{subtitle}")
    
    return home_path,subtitle


def translate(input_video,output_type,model):
    # 默认有临时目录
    home_path = "\\".join(input_video.split("\\")[:-1])
    input_name = input_video.split("\\")[-1].split(".")[0]
    audio_path = input_video.split(".")[0]
    output_video =  audio_path + "_subtitled.mp4"
    output_text = f"{audio_path}.{output_type}"

    # 抽取音频 保存 mp3
    audio_file = video2mp3(input_video)

    # 抽取字幕
    output_types = set(['vtt',output_type])
    _, subtitle = audio2srt(audio_file,model,output_types,input_name,home_path)

    # 读取字幕
    with open(output_text,'r') as f:
        output_content = "".join(f.readlines())

    # 视频 + 字幕 合成
    os.system(f"ffmpeg -i {input_video} -vf subtitles={subtitle} {output_video}")

    return  output_video, output_content,audio_file