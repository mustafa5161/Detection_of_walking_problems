from .tools.interface_design import create_design
from .tools.interface_functions import video_verification_and_upload

def launch_interface_get_video():
    window, istruction_label, upload_button = create_design()

    selected_video = [None]

    def clicked_upload_button():
        video_verification_and_upload(window, selected_video)

    upload_button.config(command=clicked_upload_button)

    window.mainloop()

    return selected_video[0]