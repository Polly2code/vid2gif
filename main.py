from moviepy.editor import VideoFileClip
import os

def convert_video_to_gif(video_path, output_path=None, resize_factor=1.0, speed_factor=1.0):
    """
    Convert a video file to GIF format
    
    Args:
        video_path (str): Path to the input video file
        output_path (str, optional): Path for the output GIF file. If None, uses the same name as video
        resize_factor (float): Factor to resize the video (1.0 = original size, 0.5 = half size)
        speed_factor (float): Factor to adjust speed (1.0 = original speed, 2.0 = twice as fast)
    """
    try:
        # If no output path is specified, create one based on the input file
        if output_path is None:
            output_path = os.path.splitext(video_path)[0] + '.gif'

        # Load the video file
        video_clip = VideoFileClip(video_path)
        
        # Resize if needed
        if resize_factor != 1.0:
            video_clip = video_clip.resize(resize_factor)
            
        # Adjust speed if needed
        if speed_factor != 1.0:
            video_clip = video_clip.speedx(speed_factor)

        # Convert to GIF
        video_clip.write_gif(output_path, fps=20)
        
        # Close the video clip to free up resources
        video_clip.close()
        
        print(f"Successfully converted {video_path} to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    video_path = input("Enter the path to your video file: ")
    resize = input("Enter resize factor (1.0 for original size, 0.5 for half size, etc.): ")
    speed = input("Enter speed factor (1.0 for original speed, 2.0 for twice as fast, etc.): ")
    
    try:
        resize_factor = float(resize)
    except ValueError:
        resize_factor = 1.0
        print("Invalid resize factor, using original size")
        
    try:
        speed_factor = float(speed)
    except ValueError:
        speed_factor = 1.0
        print("Invalid speed factor, using original speed")
    
    convert_video_to_gif(video_path, resize_factor=resize_factor, speed_factor=speed_factor)
