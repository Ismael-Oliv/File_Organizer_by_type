import os
import shutil

class Organize_Services:
    def __init__(self, source, destination_path) -> None:
        self.destination = destination_path.text()
        self.source  = source.text()
        self.folders = []

    def organize_file_by_type(self, progress_bar, status_label):

        if self.destination == "":
            self.destination = self.source

        for dir_path, dir_names, files_names in os.walk(self.source):
            total_file = len(files_names)
            line= 0
            for file in files_names:
                _, ext = file.split(".")

                if ext not in self.folders:
                    self.folders.append(ext)
                    os.mkdir(path=os.path.join(self.destination, ext))

                shutil.move(src=os.path.join(self.source, file),
                            dst=os.path.join(self.source, ext, file)
                )

                status_label.setText("Arquivo : " + file)
                line += 1
                total_process = (line/total_file) * 100
                progress_bar.setValue(float(total_process))

