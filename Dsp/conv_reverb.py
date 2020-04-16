def conv_reverb(signal,IR):
    import numpy as np 
    from matplotlib import pyplot as plt 
    import soundfile as sf 
    import sounddevice as sd 
    print("Runing program...")
    audio,fs = sf.read(signal)
    IR,fs2 = sf.read(IR)
    if audio.ndim==1:
        IRL=IR[:,0]
        print(IRL.ndim)
        signal_out=np.convolve(audio,IRL)
        signal_out=np.transpose(signal_out)
        sf.write('prueba.wav',signal_out,fs)
    else:
            
        IRL=IR[:,0]
        IRR=IR[:,1]
        audioL=audio[:,0]
        audioR=audio[:,1]
        signal_outL=np.convolve(audioL,IRL)
        signal_outR=np.convolve(audioR,IRR)
        signal_out=np.vstack((signal_outL,signal_outR))
        signal_out=np.transpose(signal_out)
        sf.write('prueba.wav',signal_out,fs)

    print(signal_out.shape)
    return(signal_out)

conv_reverb("Melo 2.wav","1st_baptist_nashville_balcony.wav")
