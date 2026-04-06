import os
import random
import shutil

def sample_images(sourceDir, targetDir, numSamples=10):
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    images = [f for f in os.listdir(sourceDir) if f.lower().endswith(('.jpg', '.png'))]

    selected = random.sample(images, min(numSamples, len(images)))

    for img in selected:
        src = os.path.join(sourceDir, img)
        dst = os.path.join(targetDir, img)
        shutil.copy(src, dst)

    print(f"Copied {len(selected)} images to {targetDir}")


if __name__ == "__main__":
    sourceDir = "images"
    targetDir = "sample-images"
    sample_images(sourceDir, targetDir)