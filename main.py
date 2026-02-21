import asyncio

import edge_tts
import gradio as gr
import soundfile as sf
import torch
import torchaudio
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from moviepy.config import change_settings
from moviepy.editor import (
    AudioFileClip,
    CompositeVideoClip,
    ImageClip,
    TextClip,
    concatenate_videoclips,
)

# 1. System Config: Fix for ImageMagick in WSL2
change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

import brain
import config


async def production_pipeline(img_list, prod_name, extra_notes):
    """
    Takes multiple images, a product name, and user keywords to create a custom ad.
    """
    config.initialize_system()
    
    if not img_list:
        return None, "Please upload at least one image."

    # --- PHASE 1: DYNAMIC AI BRAIN ---
    # The brain now uses 'prod_name' and 'extra_notes' to write the script
    headline, script, details = brain.generate_ad_assets(img_list[0].name, prod_name, extra_notes)
    
    # --- PHASE 2: VOICE GENERATION ---
    raw_audio_path = "raw_voice.mp3"
    await edge_tts.Communicate(script, "ar-EG-SalmaNeural").save(raw_audio_path)
    
    # --- PHASE 3: GPU AUDIO POLISH ---
    audio_data, sample_rate = sf.read(raw_audio_path)
    waveform = torch.FloatTensor(audio_data).t()
    if waveform.ndim == 1: waveform = waveform.unsqueeze(0)
    waveform = waveform.to("cuda")
    waveform = waveform / (torch.max(torch.abs(waveform)) + 1e-7) # GPU Normalization
    
    polished_audio_path = "polished_voice.wav"
    sf.write(polished_audio_path, waveform.to("cpu").numpy().T, sample_rate)
    
    # --- PHASE 4: MULTI-IMAGE VIDEO MONTAGE ---
    output_video_path = config.get_unique_path(prod_name)
    audio_clip = AudioFileClip(polished_audio_path)
    
    duration_per_img = audio_clip.duration / len(img_list)
    
    clips = []
    for img in img_list:
        clip = (ImageClip(img.name)
                .set_duration(duration_per_img)
                .set_fps(30)
                .crossfadein(0.5))
        clips.append(clip)
    
    video_base = concatenate_videoclips(clips, method="compose")
    
    # Arabic Text Overlay (Reshaped for RTL)
    reshaped_headline = get_display(reshape(headline))
    try:
        txt_layer = (TextClip(reshaped_headline, fontsize=60, color='gold', 
                              font='DejaVu-Sans-Bold', stroke_color='black', stroke_width=2,
                              method='caption', size=(video_base.w*0.8, None))
                     .set_duration(video_base.duration)
                     .set_position(('center', 0.8), relative=True))
        final_video = CompositeVideoClip([video_base, txt_layer]).set_audio(audio_clip)
    except:
        final_video = video_base.set_audio(audio_clip)

    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    
    return output_video_path, f"AI Script for {prod_name}:\n\n{script}"

# GRADIO INTERFACE
app = gr.Interface(
    fn=production_pipeline,
    inputs=[
        gr.File(file_count="multiple", label="Upload Product Photos"), 
        gr.Textbox(label="Product Name"),
        gr.Textbox(label="Keywords/Instructions (e.g., 'Free delivery', 'Limited time')")
    ],
    outputs=[
        gr.Video(label="Final Egyptian Montage"), 
        gr.Textbox(label="AI Production Log")
    ],
    title="Fahlawi AI Multi-Pro 🚀",
    description="Drag images, name your product, and give AI keywords to create your ad."
)

if __name__ == "__main__":
    app.launch()