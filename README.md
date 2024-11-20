# RANSAC Segmentation

This project focuses on segmentation and geometric primitive fitting using RANSAC (Random Sample Consensus) for LiDAR point cloud. It specifically explores detecting planes and cylinders in 3D point clouds.

## Features

- **Two RANSAC Implementations**:
  - **Geometric RANSAC**: A basic RANSAC implementation focused on direct geometric fitting.
  - **Normal RANSAC**: An enhanced version utilizing surface normals for improved segmentation.
- **Geometric Primitive Fitting**:
  - Plane fitting.
  - Cylinder fitting with RANSAC.
- **Program Files**:
  - **Geometric RANSAC**: `Geometric_RANSAC.ipynb`
  - **Normal RANSAC**: `Normal_RANSAC.ipynb`
- **Point Clouds**:
   Three point clouds are included (.pcd files)
  - **scene1.pcd**
  - **scene2.pcd**
  - **scene3.pcd**
 
- **Statistics**:
  Additional statistics can be viewed in:
    - `SCENE_1.ipynb`
    - `SCENE_2.ipynb`
    - `SCENE_3.ipynb`

## Usage

After cloning the repository, start either `Geometric_RANSAC.ipynb` or `Normal_RANSAC.ipynb`. Run the entire kernel to initialize all methods and execute a sample run. Make changes and experiment in the **Testing Ground** section in each file.
