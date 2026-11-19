# Parking Lot Detector

Figures out which spots in a parking lot are free from overhead drone footage. It's all plain OpenCV image processing, no trained model. Every spot gets a box drawn over it: green if it's open, blue if a car is parked there. The number on each box is the pixel count it used to make that call.

## How it works

The spot locations are marked by hand once and saved to `data/CarParkData`. After that, each frame of the video goes through the same steps:

1. Convert to grayscale and blur it slightly
2. Adaptive threshold, so edges (mostly cars) come out white and empty asphalt stays black
3. Median blur to clean up noise like painted lines and cracks, then dilate so cars turn into solid blobs
4. Crop each saved spot and count the white pixels in it

An empty spot has almost no edges in it and a car has a lot, so if the count goes over the threshold (600 for a regular box) the spot is marked as taken. Works better than you'd expect for something this simple.

## Files

| File | What it is |
| --- | --- |
| `main.py` | Runs the detector on the video |
| `ParkingLotMasker.py` | Tool for marking where the spots are |
| `data/parking_lot_video.mp4` | The drone footage |
| `data/Parking_Lot_Mask.jpg` | A still frame from the video, used when marking spots |
| `data/CarParkData` | Saved spot positions (pickled list of `(x, y, type)`) |

## Running it

Needs Python 3 and:

```bash
pip install opencv-python cvzone numpy
```

Then from the project folder:

```bash
python main.py
```

The video loops forever and there's no quit key, so stop it with Ctrl+C in the terminal.

**Note:** the file paths in both scripts use Windows backslashes (`data\\parking_lot_video.mp4`). On macOS or Linux, switch them to forward slashes or it won't find the files.

## Marking spots

```bash
python ParkingLotMasker.py
```

- **Left click** adds a regular spot (70x30 box)
- **Middle click** adds a shorter box that uses a different threshold (1400)
- **Right click** removes the box under the cursor

Each click saves straight to `data/CarParkData`, so delete that file first if you want to start over.

## Limitations

- Spot positions are fixed, so the camera has to stay still.
- The thresholds were tuned by eye for this one video. Different lighting, shadows or a different lot will need them adjusted in `main.py`.
