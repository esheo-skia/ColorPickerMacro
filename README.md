# label_colors_macro.py

A lightweight internal macro for 3D Slicer that automatically assigns predefined colors to anatomical segments based on their names.  
Developed to streamline repetitive labeling tasks in segmentation workflows.

This script adds a **“Apply Color” button** to the Segment Editor. When clicked, it applies consistent, pre-defined colors to structures such as arteries, veins, and ureters.

---

## Purpose

While working with dozens of segmentations, I needed a quick way to:

- Assign consistent colors across datasets
- Avoid manual selection from the color picker
- Reduce labeling time and prevent mistakes

This macro was developed and used in real-world labeling workflows for clinical AI datasets.  
It is **not intended for public distribution**, but serves as a personal automation utility.

---

## Built-in Color Logic

No external configuration needed — segment names and colors are defined inside the script:

| Group | Color     | Segment Names |
|-------|-----------|----------------|
| Arteries | `#af0000` | `Ao`, `SMA`, `RA`, `EIA_left`, ... |
| Veins    | `#0000ff` | `IVC`, `SMV`, `CIV_right`, ... |
| Ureter   | `#ffff00` | `ureter` |

- If a segment name does not match the predefined list, it will be skipped silently.

---

## File Structure

```
label-colors-macro/
├── label_colors_macro.py         # Main macro logic
├── segment_ui.py                 # Adds the button to Segment Editor
├── slicerrc_template.py          # Template to auto-load button at Slicer startup
├── README.md                     # This file
└── screenshots/                  # (Optional) UI screenshots
    └── ColorPickerMacro.gif
```

---

## How to Use

1. Copy `slicerrc_template.py` to your user home directory and rename it to `.slicerrc.py`.

   Example (Windows):
   ```
   C:\Users\YOUR_USERNAME\.slicerrc.py
   ```

2. Restart 3D Slicer.

3. Open the **Segment Editor** → the **Apply Color** button should appear at the bottom.

4. Click the button to apply the predefined colors to any matching segment names.

---

## 🖼 UI Screenshots

### Demo – Color Auto-Assignment in Action

![ColorPickerMacro Demo](screenshots/ColorPickerMacro.gif)

---

## Author

**Eunseo Heo (esheo-skia)**<br>
*Software Developer — Imaging Tools & Automation*

* **Contact:** [heunseo1787@gmail.com]
* **GitHub:** [https://github.com/esheo-skia]

---

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

---

## Notes

- This tool was developed and validated in real-world annotation workflows.
- Designed to be minimal, robust, and portable for internal use.
- Initial commit was made under my secondary GitHub account `heunseoh` for local testing.  
  All code, design, and updates are authored by myself and maintained on `esheo-skia`.
