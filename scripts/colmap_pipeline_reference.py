"""
Logical structure of the COLMAP pipeline used in this project.
Represents what was executed via GUI.
"""

def featureExtraction():
    print("Extract SIFT features from all images")
    print("Store keypoints in database")

def featureMatching(method="exhaustive"):
    if method == "exhaustive":
        print("Match all image pairs")
    elif method == "sequential":
        print("Match neighboring frames only")
    elif method == "guided":
        print("Apply geometric filtering to matches")

def reconstruction():
    print("Estimate camera poses")
    print("Triangulate 3D points")
    print("Build sparse point cloud")

def runPipeline(method):
    featureExtraction()
    featureMatching(method)
    reconstruction()


if __name__ == "__main__":
    for method in ["exhaustive", "sequential", "guided"]:
        print(f"\nRunning {method} pipeline\n")
        runPipeline(method)