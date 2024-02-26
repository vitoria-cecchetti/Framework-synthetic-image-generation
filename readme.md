# Framework for Automated Synthetic Image Generation for Vehicle Detection

Vitória Biz Cecchetti, Bruno J. Souza, Roberto Z. Freire

International Conference on Control, Robotics Engineering and Technology (CRET) 2023

---

### Pre requisites

This code was developed with Python 3.10 and Blender 3.9.

### Running the code

To run the image generation code, you must have the generation.py file and you .blend file in the same folder, then running the generation.py code can be done with the following command in the powershell/bash window:

```
blender --background your_blender_model.blend --python generation.py -- SELECTED VEHICLE your/output/path -c {PARAMETER_1} -r {PARAMETER_2} -f {PARAMETER_3} -t {PARAMETER_4} -p {PARAMETER_5} -d {PARAMETER_6}
```

Where:

- PARAMETER_1: Desired camera view (0: oblique view, 1: parallel view).
- PARAMETER_2: Rain intensity (number of rain drops in the images).
- PARAMTER_3: Fog intensity (0: complete fog, 1: no fog).
- PARAMETER_4: Tree occlusion percentage.
- PARAMETER_5: Light pole occlusion percentage.
- PARAMETER_6: Light intensity (0: night, 1: day).

Command ```generation.py --help``` for further information.
