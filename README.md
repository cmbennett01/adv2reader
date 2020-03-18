adv2reader
==========

This package provides a 'reader' for .adv (AstroDigitalVideo) files.

The specification for Astro Digital Video files can be 
found at: <http://www.astrodigitalvideoformat.org/spec.html>

To install this package on your system:

    pip install Adv2reader

Then, sample usage from within your Python code is:

    from Adv2reader.Adv2File import Adv2reader
    from pathlib import Path
    
    rdr = None
    try:
        # Create a platform agnostic path to your .adv file (use forward slashes)
        file_path = str(Path('path/to/your/file.adv'))  # Python will make Windows version as needed
        
        # Create a 'reader' for the given file
        rdr = Adv2reader(file_path)
    
    except AdvLibException as adverr:
        print(repr(adverr))
        exit()
    
    except IOError as ioerr:
        print(repr(ioerr))
        exit()

Now that the file has been opened and a 'reader' (rdr) created for it, 
there are instance variables available that will be useful.
Here is how to print some of those out:

    print(f'Width: {rdr.Width}  Height: {rdr.Height}  NumMainFrames: {rdr.CountMainFrames}')

There is also an composite instance variable called `FileInfo` which gives access to all
of the values defined in the structure `AdvFileInfo` (there are 20 of them).

For example:

    print(rdr.FileInfo.UtcTimestampAccuracyInNanoseconds)
    
To get (and show) the file metadata (returned as a Dict[str, str]):

    print(f'\nADV_FILE_META_DATA:')
    meta_data = rdr.getAdvFileMetaData()
    for key in meta_data:
        print(f'    {key}: {meta_data[key]}')
        
The main thing that one will want to do is read image data, timestamps, and frame status information
from image frames.

Continuing with the example and assuming that the adv file contains a MAIN stream (it
might also contain a CALIBRATION stream):
  
    
    for frame in range(rdr.CountMainFrames):
        # To get frames from a CALIBRATION stream, use rdr.getCalibImageAndStatusData()
        # status is a Dict[str, str]
        
        err, image, frameInfo, status = rdr.getMainImageAndStatusData(frameNumber=frame)

        if not err:
            print(f'\nframe: {frame} STATUS:')
            print(frameInfo.DateString, frameInfo.StartOfExposureTimestampString)
            for entry in status:
                print(f'    {entry}: {status[entry]}')
        else:
            print(err)

`err` is a string that will be empty if image bytes and metadata where successfully extracted.
In that case, `image` will contain a numpy array of uint16 values. If `err` is not empty, it will contain
a human-readable description of the error encountered.

The 'shape' of image will be `image[Height, Width]` for grayscale images. Color video
files are not yet supported.

Finally, the file should closed as in the example below:

    print(f'closeFile returned: {rdr.closeFile()}')
    rdr = None
    
The value returned will be the version number (2) of the file closed or 0, which indicates an attempt to close a file that was
already closed.
