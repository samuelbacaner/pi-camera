from time import sleep
from picamera import PiCamera
from datetime import datetime
import signal
import os

class InterruptibleRecording():

    def __init__(self):
        self.camera=PiCamera(framerate=10)
        self.camera.resolution=(640, 480)
        signal.signal( signal.SIGUSR1, lambda signal, frame: self._interruptHandler() )
        self.terminated = False

    def _interruptHandler(self):
        self.terminated = True
        if self.camera.recording:
            self.camera.stop_recording()
            print("Stopped recording... (" + InterruptibleRecording._getTimestamp() + ")")

    @staticmethod
    def _getTimestamp():
            return datetime.now().strftime("%Y-%m-%d::%H:%M:%S")

    @staticmethod
    def _getFileName():
        return '/data/' + InterruptibleRecording._getTimestamp() + ".h264"

    def start(self):
        print('My PID is:', os.getpid())

        while not self.terminated:
            fileName = InterruptibleRecording._getFileName()
            print("Recording to new file: " + fileName)
            self.camera.start_recording(fileName)
            self.camera.wait_recording(5)
            # signal handler will have likely already stopped the camera
            if self.camera.recording:
                self.camera.stop_recording()

        print("Exiting...")

    


