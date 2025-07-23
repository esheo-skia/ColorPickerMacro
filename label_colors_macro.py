import slicer

def forceApplyLabelColors():
    label_color_map = {}

    # Red: Arterial structures
    red_labels = [
        "Ao", "SMA", "IMA",
        "RA", "RA_left", "RA_right",
        "CIA", "CIA_left", "CIA_right",
        "EIA", "EIA_left_all", "EIA_left", "SCIA_left", "SIEA_left",
        "EIA_right_all", "EIA_right", "SCIA_right", "SIEA_right",
        "IIA", "IIA_left", "IIA_right"
    ]
    red_color = (0.686, 0.0, 0.0)  # #af0000
    for label in red_labels:
        label_color_map[label] = red_color

    # Blue: Venous structures
    blue_labels = [
        "IVC", "SMV",
        "RV", "RV_left", "RV_right",
        "CIV", "CIV_left", "CIV_right",
        "EIV", "EIV_left", "EIV_right",
        "IIV", "IIV_left", "IIV_right"
    ]
    blue_color = (0.0, 0.0, 1.0)  # #0000ff
    for label in blue_labels:
        label_color_map[label] = blue_color

    # Yellow: Ureter
    label_color_map["ureter"] = (1.0, 1.0, 0.0)  # #ffff00

    # Automatically select the first available segmentation node
    segmentationNodes = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')
    if not segmentationNodes:
        slicer.util.errorDisplay("No segmentation node found.")
        return

    segmentationNode = segmentationNodes[0]
    segmentation = segmentationNode.GetSegmentation()

    for segmentId in segmentation.GetSegmentIDs():
        segment = segmentation.GetSegment(segmentId)
        name = segment.GetName()
        if name in label_color_map:
            color = label_color_map[name]
            segment.SetColor(color)
            print(f"Applied color: {name} → {color}")
        else:
            print(f"No predefined color for (skipped): {name}")

    segmentationNode.Modified()
    print("Color application completed.")
