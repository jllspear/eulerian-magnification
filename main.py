import eulerian_magnification as em
import sys

print(sys.version)

source_path = './data/car_engine.avi'
# vid, fps = em.load_video_float(source_path)
# em.show_frequencies(vid, fps)

vid, fps = em.load_video_float(source_path)
vid_out = em.eulerian_magnification(vid, fps,
        freq_min=50.0 / 60.0,
        freq_max=1.0,
        amplification=50,
        pyramid_levels=3
)

em.show_frequencies(vid, fps)

# em.io.save_video(vid_out, fps, save_filename='./data/baby_out.avi')
