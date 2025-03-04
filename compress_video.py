import glob
import os
import subprocess

EXTENSION = "mov"


def speed_up_video(input_file):
    name, _ = os.path.splitext(input_file)
    output_file = f"{name}-compressed.{EXTENSION}"

    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-filter_complex",
        "[0:v]setpts=0.8*PTS[v];[0:a]atempo=1.25[a]",
        "-map",
        "[v]",
        "-map",
        "[a]",
        output_file,
    ]

    print(f"Processing {input_file} -> {output_file}")

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        os.remove(input_file)
        os.rename(output_file, input_file)
        print(f"Finished: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_file}: {e}")


def process_files():
    files = sorted(glob.glob(f"*.{EXTENSION}"))

    for file in files:
        if "compressed" not in file.lower():
            speed_up_video(file)

    print("Batch processing complete!")


process_files()
