import InterruptibleRecording
DEBUG_ADDRESS = ('0.0.0.0', 3000)

def doRun(devMode: bool=False):
    print('Running {}...'.format('in DEV mode ' if devMode else ''))
    interruptibleRecording = InterruptibleRecording.InterruptibleRecording()
    interruptibleRecording.start()
    

if __name__ == '__main__':
    import sys
    devMode = False
    if '--dev' in sys.argv:
        devMode = True

        # enable VS Code debugging via ptvsd
        import ptvsd
        print('Enabling debug on {}'.format(DEBUG_ADDRESS))
        ptvsd.enable_attach(address=DEBUG_ADDRESS, redirect_output=True)
    
    doRun(devMode)

