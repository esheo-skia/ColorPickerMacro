import slicer
import qt
import os

# Load only the color macro script
def loadColorMacro():
    macro_dir = r"C:\Users\Lenovo\Documents\SlicerExtensions\label_colors"  # Modify this path as needed
    exec(open(os.path.join(macro_dir, "label_colors_macro.py")).read(), globals())

def addColorApplyButton():
    loadColorMacro()  # Load the color macro function

    mainWindow = slicer.util.mainWindow()
    statusBar = mainWindow.statusBar()

    if not hasattr(slicer, "customColorButton"):
        slicer.customColorButton = qt.QHBoxLayout()
        w = qt.QWidget()
        w.setLayout(slicer.customColorButton)
        statusBar.layout().addWidget(w)

        btn = qt.QPushButton("Apply Color")
        btn.setToolTip("Apply predefined colors to matching segment names.")
        btn.connect("clicked()", forceApplyLabelColors)
        slicer.customColorButton.addWidget(btn)

        print("Color apply button successfully created.")

# Execute immediately
addColorApplyButton()
